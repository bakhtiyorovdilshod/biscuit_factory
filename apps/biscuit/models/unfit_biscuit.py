from django.db import models

from apps.biscuit.models import Biscuit


class UnfitBiscuit(models.Model):
    statuses = (
        ('recyclable', 'recyclable'),
        ('unrecyclable', 'unrecyclable')
    )
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=statuses)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def set_total_price(self):
        biscuit = Biscuit.objects.get(id=self.biscuit.id)
        self.total_price = self.quantity * biscuit.price

    def __str__(self):
        return str(self.id)