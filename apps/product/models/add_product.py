from django.db import models
from .product import Product
from .supplier import Supplier

from apps.user.models.account import Account


class AddProduct(models.Model):
    type_currency = (
        ('SOM', 1),
        ('USD', 2)
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=10, choices=type_currency)
    price = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    warehouseman = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def set_total_price(self):
        self.total_price = self.quantity * self.price

    def __str__(self):
        return str(self.id)

