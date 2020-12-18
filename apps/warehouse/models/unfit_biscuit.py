import decimal

from django.db import models
from apps.biscuit.utils.biscuit import get_biscuit_price


class WareHouseUnfitBiscuit(models.Model):
    statuses = (
        ('recyclable', 'recyclable'),
        ('unrecyclable', 'unrecyclable')
    )
    from apps.biscuit.models import Biscuit
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4, default=decimal.Decimal(0))
    unit_of_measurement = models.CharField(max_length=200, default='kg', blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=4, default=decimal.Decimal(0))
    status = models.CharField(max_length=100, choices=statuses, blank=True, null=True)
    currency = models.CharField(max_length=10, default='So\'m')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def add_quantity(self, value):
        self.quantity += value

    def subtract_quantity(self, value):
        self.quantity -= value

    def set_total_price(self):
        price = get_biscuit_price(self.biscuit)
        self.total_price = price * self.quantity

    def __str__(self):
        return str(self.biscuit) + " " + str(self.status)