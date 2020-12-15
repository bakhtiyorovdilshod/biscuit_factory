import decimal

from django.db import models

from apps.biscuit.models.biscuit import Biscuit, PriceList


class WareHouseBiscuit(models.Model):
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    average_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    unit_of_measurement = models.CharField(default='kg', max_length=200, blank=True, null=True)
    currency = models.CharField(max_length=10, default='So\'m')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def set_average_price(self):
        self.average_price = self.total_price/self.quantity

    def set_total_price(self):
        price = PriceList.objects.filter(biscuit=self.biscuit).order_by('-id').first().price
        if price is None:
            price = Biscuit.objects.get(id=self.biscuit.id).price
        self.total_price = price * self.quantity

    def add_quantity(self, value):
        self.quantity += value

    def subtract_quantity(self, value):
        self.quantity -= value

    def __str__(self):
        return str(self.biscuit)