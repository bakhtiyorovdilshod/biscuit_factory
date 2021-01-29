from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.order.views.order import ClientOrderModelViewSet

router = SimpleRouter()
router.register('orders', ClientOrderModelViewSet)


urlpatterns = [
    path('client/', include(router.urls)),



]