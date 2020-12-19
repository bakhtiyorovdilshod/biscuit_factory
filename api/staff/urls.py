from django.urls import path, include
from api.staff.views.salary import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router_two = SimpleRouter()


router.register('percentage', SalaryPercentageModelViewSet)
router_two.register('', StaffSalaryModelSerializerModelViewSet)

urlpatterns = [
    path('salary/', include(router.urls)),
    path('salary/', include(router_two.urls))

]



