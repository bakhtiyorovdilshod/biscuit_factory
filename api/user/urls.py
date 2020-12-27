from django.urls import path, include
from api.user.views.account import RegisterUserAPIView, LoginUserAPIView, FilterUserAPIView, AccountListAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('list', AccountListAPIView)


urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register user'),
    path('sign_in/', LoginUserAPIView.as_view(), name='sign in user'),
    path('filter/', FilterUserAPIView.as_view(), name='filter users with their role'),
    path('account/', include(router.urls))

]