from django.urls import path, include
from api.staff.views.salary import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router_two = SimpleRouter()


router.register('percentage', SalaryPercentageModelViewSet)
router_two.register('add', StaffBiscuitModelViewSet)


urlpatterns = [
    path('salary/', include(router.urls)),
    path('biscuit/', include(router_two.urls)),
    path('salary/list/', StaffSalaryListAPIView.as_view(), name='staff salary list'),
    path('salary/detail/<int:pk>/', StaffSalaryDetailAPIView.as_view(), name='staff salary detail')

]



