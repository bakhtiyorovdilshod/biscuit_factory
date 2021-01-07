import decimal

from django.db import models

from apps.biscuit.models import Biscuit, PriceList
from apps.user.models import Account


class ProduceBiscuit(models.Model):
    status_type = (
        ('unpaid', 'unpaid'),
        ('paid', 'paid')
    )
    type_of_calculate = (
        ('un_calculate', 'un_calculate'),
        ('calculated', 'calculated')
    )
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    currency = models.CharField(default='so\'m', max_length=200, blank=True, null=True)
    status = models.CharField(max_length=50, choices=status_type, default='unpaid', blank=True, null=True)
    for_price= models.CharField(max_length=50, choices=type_of_calculate, default='un_calculate')
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def set_total_price(self):
        price = PriceList.objects.filter(biscuit=self.biscuit).order_by('-id').first().price
        self.total_price = price * self.quantity

    def __str__(self):
        return str(self.biscuit)


class ProduceBiscuitLog(models.Model):
    status_type = (
        ('completed', 'completed'),
        ('pending', 'pending')
    )
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    staff = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    currency = models.CharField(default='so\'m', max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, default='pending', choices=status_type, blank=True, null=True)
    produce_biscuit_id = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.produce_biscuit_id)





