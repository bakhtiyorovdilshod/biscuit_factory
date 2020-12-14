from django.db import models


class Biscuit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    unit_of_measurement = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class PriceList(models.Model):
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0, blank=True, null=True)
    currency = models.CharField(default='so\'m', max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.biscuit)
