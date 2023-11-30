from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status

from core.pagination import PageLimitPagination
from product.models import Dialer, DealerPrice, Product, ProductDialerKey
from .serializers import DialerSerializer, DialerPriceSerializer, ProductSerializer


class DialerViewSet(ReadOnlyModelViewSet):
    queryset = Dialer.objects.all()
    serializer_class = DialerSerializer


class DealerPriceViewSet(ReadOnlyModelViewSet):
    queryset = DealerPrice.objects.all()
    serializer_class = DialerPriceSerializer
    pagination_class = PageLimitPagination

    @action(detail=True)
    def get_data_for_marking(self, request, pk):
        obj = get_object_or_404(DealerPrice, pk=pk)
        # болванка для тестирования
        return Response(ProductSerializer(Product.objects.all()[:5], many=True).data)

    @action(
        methods=["post"], detail=True, url_path="set_link_with_product/(?P<pr_id>\d+)"
    )
    def set_link_with_product(self, request, pk, pr_id):
        ob_dprice = get_object_or_404(DealerPrice, pk=pk)
        # создание новой связки
        if int(pr_id):
            ob_prod = get_object_or_404(Product, pk=pr_id)
            ob_key = ProductDialerKey.objects.get_or_create(
                product_key=ob_dprice, product_id=ob_prod
            )
            return Response(
                data=DialerPriceSerializer(ob_dprice).data, status=status.HTTP_200_OK
            )

        # удаление
        else:
            ProductDialerKey.objects.filter(product_key=ob_dprice).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageLimitPagination
