from django.db import models

from apps.biscuit.models import Biscuit
from apps.user.models import Account


class ProduceBiscuit(models.Model):
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    staff = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.PositiveIntegerField(default=0)
    currency = models.CharField(default='so\'m', max_length=200, blank=True, null=True)

    def set_total_price(self):
        biscuit = Biscuit.objects.get(id=self.biscuit.id)
        self.total_price = self.quantity * biscuit.price

    def __str__(self):
        return str(self.biscuit)