from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DialerViewSet, DealerPriceViewSet

router_v1 = DefaultRouter()

router_v1.register('dialers', DialerViewSet, basename='dialers')
router_v1.register('dialer-prices', DealerPriceViewSet, basename='dialer-prices')

urlpatterns = [
    path('', include(router_v1.urls))
]