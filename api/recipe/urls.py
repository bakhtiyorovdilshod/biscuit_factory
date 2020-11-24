from django.urls import path, include
from api.recipe.views.biscuit_recipe import RetseptListAPIView, RetseptDetailAPIView


urlpatterns = [
    path('', RetseptListAPIView.as_view(), name='biscuit recipe create'),
    path('update_or_detail/', RetseptDetailAPIView.as_view(), name='biscuit recipe update and get detail')


]

