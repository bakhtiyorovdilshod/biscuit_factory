import decimal

from django.db import models

from apps.biscuit.models import Biscuit, PriceList
from apps.user.models import Account


class ClientOrder(models.Model):
    status_type = (
        ('pending', 'pending'),
        ('completed', 'completed')
    )
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    comment = models.TextField()
    status = models.CharField(max_length=50, choices=status_type, default='pending', blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.biscuit)
