import decimal

from django.db import models

from api.biscuit.utils.price import get_price
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
        price = get_price(self.biscuit).order_by('-id')
        if price.exists():
            price = price.first().price
            self.total_price = self.quantity * price
            return True
        else:
            return False

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