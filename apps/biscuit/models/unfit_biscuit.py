import decimal

from django.db import models
from apps.biscuit.models import Biscuit, PriceList



class UnfitBiscuit(models.Model):
    statuses = (
        ('recyclable', 'recyclable'),
        ('unrecyclable', 'unrecyclable')
    )
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=statuses)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def set_total_price(self):
        from apps.biscuit.utils.biscuit import get_biscuit_price
        price = get_biscuit_price(self.biscuit)
        self.total_price = self.quantity * price

    def __str__(self):
        return str(self.id)


class AddUnFitBiscuitLog(models.Model):
    statuses = (
        ('recyclable', 'recyclable'),
        ('unrecyclable', 'unrecyclable')
    )
    unfit_biscuit_id = models.PositiveIntegerField(default=0)
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    status = models.CharField(max_length=100, choices=statuses)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.unfit_biscuit_id)