from django.db import models
from apps.supplier.models.supplier import Supplier


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    unit_of_measurement = models.CharField(default='kg', max_length=200, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ManufacturedProduct(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    unit_of_measurement = models.CharField(default='kg', max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


