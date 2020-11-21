from django.urls import path, include

from api.product.views.add_product import ProductAddModelViewSet
from api.product.views.product import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router_one = SimpleRouter()
router.register('', ProductModelViewSet)
router_one.register('quantity', ProductAddModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', include(router_one.urls))


]