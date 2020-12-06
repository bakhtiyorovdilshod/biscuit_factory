from django.urls import path
from api.user.views.account import RegisterUserAPIView, LoginUserAPIView,FilterUserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register user'),
    path('sign_in/', LoginUserAPIView.as_view(), name='sign in user'),
    path('filter/', FilterUserAPIView.as_view(), name='filter users with their role')

]