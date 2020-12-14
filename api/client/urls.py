from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.client.views.client import ClientModelViewSet

router = SimpleRouter()
router.register('', ClientModelViewSet)


urlpatterns = [
    path('', include(router.urls)),



]