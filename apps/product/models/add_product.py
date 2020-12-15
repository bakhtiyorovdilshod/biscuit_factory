import decimal

from django.db import models
from .product import Product, ManufacturedProduct
from apps.supplier.models.supplier import Supplier

from apps.user.models.account import Account


class AddProduct(models.Model):
    type_currency = (
        ('SOM', 1),
        ('USD', 2)
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    currency = models.CharField(max_length=20, choices=type_currency)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    warehouseman = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def set_total_price(self):
        self.total_price = self.quantity * self.price

    def __str__(self):
        return str(self.id)


class AddManufacturedProduct(models.Model):
    type_of_calculate = (
        ('un_calculate', 'un_calculate'),
        ('calculated', 'calculated')
    )
    product = models.ForeignKey(ManufacturedProduct, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    for_price = models.CharField(max_length=50, choices=type_of_calculate, default='un_calculate')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class AddProductLog(models.Model):
    add_product_id = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.add_product_id)


class AddManufacturedProductLog(models.Model):
    manufactured_product_id = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(ManufacturedProduct, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


