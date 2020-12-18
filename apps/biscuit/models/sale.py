import decimal

from django.db import models

from apps.biscuit.models import Biscuit
from apps.client.models.client import Client


class BuyingBiscuit(models.Model):
    payment_types = (
        ('cash', 'cash'),
        ('credit_card', 'credit_card'),
        ('debt', 'debt')
    )
    delivery_status = (
        ('pending', 'pending'),
        ('take_driver', 'take_driver'),
        ('delivered', 'delivered')
    )
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    currency = models.CharField(default='so\'m', max_length=200)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    comment = models.TextField(max_length=300, blank=True, null=True)
    payment_type = models.CharField(max_length=200, default='cash', choices=payment_types)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=delivery_status, default='pending')
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.biscuit)


class BuyingBiscuitLog(models.Model):
    payment_types = (
        ('cash', 'cash'),
        ('credit_card', 'credit_card'),
        ('debt', 'debt')
    )
    sale_id = models.PositiveIntegerField(default=0)
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    currency = models.CharField(default='so\'m', max_length=200)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    comment = models.TextField(max_length=300, blank=True, null=True)
    payment_type = models.CharField(max_length=200, default='cash', choices=payment_types)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.biscuit)


class SaleBiscuitPrice(models.Model):
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    default_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.biscuit)



