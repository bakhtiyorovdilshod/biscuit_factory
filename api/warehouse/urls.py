from django.urls import path
from api.warehouse.views.product import WareHouseProductsAPIView, WareHouseManufacturedProductAPIView
from api.warehouse.views.biscuit import WareHouseBiscuitAPIView


urlpatterns = [
    path('products/', WareHouseProductsAPIView.as_view(), name='warehouse products'),
    path('biscuits/', WareHouseBiscuitAPIView.as_view(), name='warehouse biscuits'),
    path('manufacture/products/', WareHouseManufacturedProductAPIView.as_view(), name='warehouse manufactured products')

]