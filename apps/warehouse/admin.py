from django.contrib import admin
from apps.warehouse.models.product import WareHouseProduct
from apps.warehouse.models.biscuit import WareHouseBiscuit

admin.site.register(WareHouseProduct)
admin.site.register(WareHouseBiscuit)