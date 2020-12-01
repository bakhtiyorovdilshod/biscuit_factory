from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.expense.views.expense import ExpenseModelViewSet, QuantityExpenseModelViewSet

router = SimpleRouter()
router_two = SimpleRouter()

router.register('', ExpenseModelViewSet)
router_two.register('quantity', QuantityExpenseModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', include(router_two.urls))


]



