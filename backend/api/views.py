from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
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
    queryset = DealerPrice.objects.order_by('product_key', 'date').distinct('product_key')
    
    serializer_class = DialerPriceSerializer
    pagination_class = PageLimitPagination
    
    def get_object(self):
        obj = get_list_or_404(DealerPrice, product_key=self.kwargs["pk"])[0]
        return obj 

    @action(detail=True)
    def get_data_for_marking(self, request, pk):
        get_object_or_404(DealerPrice, pk=pk)
        # болванка для тестирования
        return Response(ProductSerializer(Product.objects.all()[:5], many=True).data)

    @action(
        methods=["post"], detail=True, url_path="set_link_with_product/(?P<pr_id>\d+)"
    )
    def set_link_with_product(self, request, pk, pr_id):
        ob_dprice = DealerPrice.objects.filter(product_key=pk) 
        if not ob_dprice:
            raise Http404(
                f'Не найден продукт с номером {pk}'
            )
            
        ob_dprice = ob_dprice.order_by('date')[0]

        # создание новой связки
        if int(pr_id):
            ob_prod = get_object_or_404(Product, pk=pr_id)
            ProductDialerKey.objects.get_or_create(
                product_key=ob_dprice, product_id=ob_prod
            )
            return Response(
                data=DialerPriceSerializer(ob_dprice).data, status=status.HTTP_200_OK
            )

        # удаление
        else:
            ProductDialerKey.objects.filter(product_key=ob_dprice.product_key).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageLimitPagination
