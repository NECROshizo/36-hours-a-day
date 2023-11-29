from rest_framework.viewsets import ReadOnlyModelViewSet

from product.models import DealerPrice
from .serializers import DialerPriceSerializer

class DealerPriceViewSet(ReadOnlyModelViewSet):
    queryset = DealerPrice
    serializer_class = DialerPriceSerializer