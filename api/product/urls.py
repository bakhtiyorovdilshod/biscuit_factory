from django.urls import path, include

from api.product.views.add_product import ProductAddModelViewSet, ManufacturedProductAddModelViewSet
from api.product.views.filter_product import ProductHistoryAPIView
from api.product.views.product import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router_one = SimpleRouter()
router_three = SimpleRouter()
router_four = SimpleRouter()
router.register('', ProductModelViewSet)
router_one.register('quantity', ProductAddModelViewSet)
router_three.register('list', ManufacturedProductModelViewSet)
router_four.register('add/quantity', ManufacturedProductAddModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', include(router_one.urls)),
    path('manufacture/', include(router_three.urls)),
    path('manufacture/', include(router_four.urls)),
    path('filter', ProductHistoryAPIView.as_view(), name='filter product')


]