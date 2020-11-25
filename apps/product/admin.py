from django.contrib import admin

from apps.product.models import Product, ManufacturedProduct
from apps.product.models.add_product import AddProduct

# admin.site.register(Product)
admin.site.register(ManufacturedProduct)
admin.site.register(AddProduct)

