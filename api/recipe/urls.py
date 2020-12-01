from django.urls import path, include
from api.recipe.views.biscuit_recipe import RetseptListAPIView, RetseptDetailAPIView
from api.recipe.views.manufactured_product import ManufacturedProductRetseptListAPIView, ManufacturedProductRetseptDetailAPIView


urlpatterns = [
    path('', RetseptListAPIView.as_view(), name='biscuit recipe create'),
    path('update_or_detail/', RetseptDetailAPIView.as_view(), name='biscuit recipe update and get detail'),
    path('manufactured_product/', ManufacturedProductRetseptListAPIView.as_view(), name='manufactured product recipe crearte'),
    path('manufactured_product/update_or_detail/', ManufacturedProductRetseptDetailAPIView.as_view(), name='update')


]

