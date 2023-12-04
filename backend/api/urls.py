from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DialerViewSet, DealerPriceViewSet, ProductViewSet

router_v1 = DefaultRouter()

router_v1.register("dialers", DialerViewSet, basename="dialers")
router_v1.register("dialer_prices", DealerPriceViewSet, basename="dialer_prices")
router_v1.register("products", ProductViewSet, basename="products")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
