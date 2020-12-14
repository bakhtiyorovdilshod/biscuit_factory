from django.db import models
from apps.product.models.product import Product, ManufacturedProduct, ManufacturedProductPriceList


class WareHouseProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    average_price = models.PositiveIntegerField(default=0)
    unit_of_measurement = models.CharField(default='kg', max_length=200, blank=True, null=True)
    currency = models.CharField(max_length=10, default='So\'m')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def set_average_price(self):
        self.average_price = float(self.total_price/self.quantity)

    def add_quantity(self, value):
        self.quantity += value

    def subtract_quantity(self, value):
        self.quantity -= value

    def __str__(self):
        return str(self.product)


class WareHouseManufacturedProduct(models.Model):
    manufactured_product = models.ForeignKey(ManufacturedProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    average_price = models.PositiveIntegerField(default=0)
    unit_of_measurement = models.CharField(default='kg', max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def set_average_price(self):
        self.average_price = float(self.total_price/self.quantity)

    def add_quantity(self, value):
        self.quantity += value

    def subtract_quantity(self, value):
        self.quantity -= value

    def set_total_price(self):
        price = ManufacturedProductPriceList.objects.filter(product=self.manufactured_product).order_by('-id').first().price
        self.total_price = price * self.quantity

    def __str__(self):
        return str(self.manufactured_product)