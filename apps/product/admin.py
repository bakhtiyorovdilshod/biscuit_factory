from django.contrib import admin

from apps.product.models import Product, ManufacturedProduct, ProductPriceList,ManufacturedProductPriceList
from apps.product.models.add_product import AddProduct, AddProductLog, AddManufacturedProductLog, AddManufacturedProduct

admin.site.register(AddProductLog)
admin.site.register(ManufacturedProduct)
admin.site.register(AddProduct)
admin.site.register(ProductPriceList)
admin.site.register(ManufacturedProductPriceList)
admin.site.register(AddManufacturedProductLog)
admin.site.register(AddManufacturedProduct)

