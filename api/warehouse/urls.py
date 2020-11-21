from django.urls import path
from api.warehouse.views.product import WareHouseProductsAPIView


urlpatterns = [
    path('products/', WareHouseProductsAPIView.as_view(), name='warehouse products')



]