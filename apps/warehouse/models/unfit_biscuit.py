from django.db import models


class WareHouseUnfitBiscuit(models.Model):
    statuses = (
        ('recyclable', 'recyclable'),
        ('unrecyclable', 'unrecyclable')
    )
    from apps.biscuit.models import Biscuit
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=200, default='kg', blank=True, null=True)
    total_price = models.IntegerField(default=0)
    status = models.CharField(max_length=100, choices=statuses, blank=True, null=True)
    currency = models.CharField(max_length=10, default='So\'m')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def add_quantity(self, value):
        self.quantity += value

    def subtract_quantity(self, value):
        self.quantity -= value

    def set_total_price(self):
        from apps.biscuit.models import Biscuit
        price = Biscuit.objects.get(id=self.biscuit.id).price
        self.total_price = price * self.quantity

    def __str__(self):
        return str(self.id)