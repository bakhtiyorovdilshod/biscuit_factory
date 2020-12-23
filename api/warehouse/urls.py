from django.urls import path, include
from api.warehouse.views.product import WareHouseProductsAPIView, WareHouseManufacturedProductAPIView
from api.warehouse.views.biscuit import WareHouseBiscuitAPIView
from api.warehouse.views.staff import WareHouseStaffSalaryListAPIView, WareHouseStaffSalaryDetailAPIView
from api.warehouse.views.unfit_biscuit import *
from api.warehouse.views.income import TakeMoneyModelViewSet, IncomeAPIView, ReserveMoneyDetailAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('money', TakeMoneyModelViewSet)

urlpatterns = [
    path('products/', WareHouseProductsAPIView.as_view(), name='warehouse products'),
    path('biscuits/', WareHouseBiscuitAPIView.as_view(), name='warehouse biscuits'),
    path('manufacture/products/', WareHouseManufacturedProductAPIView.as_view(), name='warehouse manufactured products'),
    path('unfit/recyclable/biscuit/', WareHouseUnfitRecyclableBiscuitListAPIView.as_view(), name='all unfit biscuit'),
    path('unfit/unrecyclable/biscuit/', WareHouseUnfitUnRecyclableBiscuitListAPIView.as_view(), name='all unfit biscuit'),
    path('take/', include(router.urls)),
    path('income/', IncomeAPIView.as_view(), name='total income'),
    path('reserve_money/', ReserveMoneyDetailAPIView.as_view()),
    path('staff/salary/lists/', WareHouseStaffSalaryListAPIView.as_view(), name='staff list'),
    path('staff/salary/detail/<int:pk>/', WareHouseStaffSalaryDetailAPIView.as_view(), name='edit staff salary')

]