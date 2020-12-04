from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.biscuit.views.biscuit import BiscuitModelViewSet

from api.biscuit.views.produce import ProduceBiscuitModelViewSet
from api.biscuit.views.unfit_biscuit import UnFitBiscuitModelViewSet

router = SimpleRouter()
router_unfit = SimpleRouter()
router.register('', BiscuitModelViewSet)
router_unfit.register('unfit', UnFitBiscuitModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', include(router_unfit.urls)),


]