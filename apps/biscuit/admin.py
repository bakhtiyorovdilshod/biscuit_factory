from django.contrib import admin

from apps.biscuit.models import ProduceBiscuit,ProduceBiscuitLog
from apps.biscuit.models.biscuit import Biscuit, PriceList
from apps.biscuit.models.unfit_biscuit import UnfitBiscuit, AddUnFitBiscuitLog
from apps.biscuit.models.sale import BuyingBiscuit, BuyingBiscuitLog, SaleBiscuitPrice



admin.site.register(Biscuit)
admin.site.register(UnfitBiscuit)
admin.site.register(ProduceBiscuit)
admin.site.register(PriceList)
admin.site.register(ProduceBiscuitLog)
admin.site.register(AddUnFitBiscuitLog)
admin.site.register(BuyingBiscuit)
admin.site.register(BuyingBiscuitLog)
admin.site.register(SaleBiscuitPrice)
