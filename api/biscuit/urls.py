from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.biscuit.views.biscuit import BiscuitModelViewSet

from api.biscuit.views.produce import ProduceBiscuitModelViewSet, FilterProduceBiscuit
from api.biscuit.views.sale import SaleBiscuitModelViewSet, FilterSaleBiscuit
from api.biscuit.views.unfit_biscuit import UnFitBiscuitModelViewSet

router = SimpleRouter()
router_unfit = SimpleRouter()
router.register('', BiscuitModelViewSet)
router_unfit.register('unfit', UnFitBiscuitModelViewSet)
router_api = SimpleRouter()
router_api_sale = SimpleRouter()
router_api.register('produce', ProduceBiscuitModelViewSet)
router_api_sale.register('sale', SaleBiscuitModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', include(router_unfit.urls)),
    path('staff/', include(router_api.urls)),
    path('company/', include(router_api_sale.urls)),
    path('saled/filter/', FilterSaleBiscuit.as_view(), name='filter saled biscuits'),
    path('produced/filter/', FilterProduceBiscuit.as_view(), name='filter produced biscuits')


]