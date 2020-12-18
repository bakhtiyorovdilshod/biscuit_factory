from django.contrib import admin

from apps.warehouse.models import WareHouseUnfitBiscuit
from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct
from apps.warehouse.models.biscuit import WareHouseBiscuit
from apps.warehouse.models.income import Income, ReserveMoney, TakeMoney, TakeMoneyLog

admin.site.register(WareHouseProduct)
admin.site.register(WareHouseBiscuit)
admin.site.register(WareHouseManufacturedProduct)
admin.site.register(WareHouseUnfitBiscuit)
admin.site.register(Income)
admin.site.register(ReserveMoney)
admin.site.register(TakeMoney)
admin.site.register(TakeMoneyLog)
