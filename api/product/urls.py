from django.urls import path, include
from api.product.views.product import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),


]