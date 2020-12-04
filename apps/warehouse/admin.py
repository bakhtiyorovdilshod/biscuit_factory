from django.contrib import admin

from apps.warehouse.models import WareHouseUnfitBiscuit
from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct
from apps.warehouse.models.biscuit import WareHouseBiscuit

admin.site.register(WareHouseProduct)
admin.site.register(WareHouseBiscuit)
admin.site.register(WareHouseManufacturedProduct)
admin.site.register(WareHouseUnfitBiscuit)
