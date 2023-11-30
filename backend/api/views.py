from rest_framework.viewsets import ReadOnlyModelViewSet

from product.models import Dialer, DealerPrice
from .serializers import DialerSerializer, DialerPriceSerializer


class DialerViewSet(ReadOnlyModelViewSet):
    queryset = Dialer.objects.all()
    serializer_class= DialerSerializer


class DealerPriceViewSet(ReadOnlyModelViewSet):
    queryset = DealerPrice.objects.all()
    serializer_class = DialerPriceSerializer