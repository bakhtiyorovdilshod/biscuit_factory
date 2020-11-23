from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.supplier.views.supplier import SupplierModelViewSet

router = SimpleRouter()
router.register('', SupplierModelViewSet)


urlpatterns = [
    path('', include(router.urls)),

]


