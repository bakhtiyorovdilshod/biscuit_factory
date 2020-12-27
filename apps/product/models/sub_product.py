import decimal

from django.db import models
from .product import Product, ManufacturedProduct
from apps.supplier.models.supplier import Supplier

from apps.user.models.account import Account


class SubProduct(models.Model):
    type_currency = (
        ('SOM', 1),
        ('USD', 2)
    )
    log_id = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=4, default=decimal.Decimal(0))
    currency = models.CharField(max_length=20, choices=type_currency, default='SOM')
    price = models.DecimalField(max_digits=20, decimal_places=4, default=decimal.Decimal(0))
    total_price = models.DecimalField(max_digits=20, decimal_places=6, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def set_total_price(self):
        self.total_price = self.quantity * self.price

    def __str__(self):
        return str(self.id)