from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status

from core.pagination import PageLimitPagination
from product.models import Dialer, DealerPrice, Product, ProductDialerKey, MLResult
from .serializers import (
    DialerSerializer, DialerPriceSerializer, DialerPriceDSSerializer, ProductSerializer, MLResultSerializer)


class DialerViewSet(ReadOnlyModelViewSet):
    queryset = Dialer.objects.all()
    serializer_class = DialerSerializer


class DealerPriceViewSet(ReadOnlyModelViewSet):
    if not settings.DB_SQL:
        queryset = DealerPrice.objects.order_by('product_key', 'date').distinct('product_key')
    else:
        queryset = DealerPrice.objects.all()

    serializer_class = DialerPriceSerializer
    pagination_class = PageLimitPagination

    def get_object(self):
        obj = get_list_or_404(DealerPrice, product_key=self.kwargs["pk"])[0]
        return obj

    @action(detail=True)
    def get_data_for_marking(self, request, pk):
        ob_dprice = DealerPrice.objects.filter(product_key=pk)
        if not ob_dprice:
            raise Http404(
                f'Не найден продукт с номером {pk}'
            )

        if MLResult.objects.filter(product_key=pk).exists():
            return Response(ProductSerializer(Product.objects.filter(product_ml__product_key=pk), many=True).data)
        else:
            raise Http404(
                'Не найден связки'
            )


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
                product_key=pk, product_id=ob_prod
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


class MatchViewSet(ReadOnlyModelViewSet):
    queryset = MLResult.objects.all()  # Неочень правильно подумать над  get_serializer_class()
    serializer_class = MLResultSerializer

    def list(self, request):
        queryset1 = DealerPrice.objects.order_by('product_key', 'date').distinct('product_key')
        queryset2 = Product.objects.all()

        serializer1 = DialerPriceDSSerializer(queryset1, many=True)
        serializer2 = ProductSerializer(queryset2, many=True)

        combined_data = {
            'dealer_priсe': serializer1.data,
            'product': serializer2.data
        }

        return Response(data=combined_data, status=status.HTTP_200_OK)

    @action(
        methods=["post"], detail=False, url_path="make_match")
    def make_match(self, request):
        MLResult.objects.all().delete()
        data = request.data["result"]
        MLResult.objects.bulk_create(
            [
                MLResult(
                    product_key=el.get("product_key"),
                    product_id=Product.objects.get(id=el.get("product_id")),
                )
                for el in data
            ]
    )

        data = request.data
        return Response(status=status.HTTP_201_CREATED)
