from django.db import models
import decimal
from apps.biscuit.models import Biscuit


class IncomeBiscuit(models.Model):
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.income)