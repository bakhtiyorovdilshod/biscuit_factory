from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.biscuit.views.biscuit import BiscuitModelViewSet

router = SimpleRouter()

router.register('', BiscuitModelViewSet)

urlpatterns = [
    path('', include(router.urls))


]