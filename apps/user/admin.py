from django.contrib import admin

from apps.user.models import User
from apps.user.models.account import Account
from apps.product.models.product import Product

admin.site.register(Account)
admin.site.register(Product)
admin.site.register(User)
