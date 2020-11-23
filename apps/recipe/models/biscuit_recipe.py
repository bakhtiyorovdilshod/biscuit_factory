from django.db import models
from apps.biscuit.models.biscuit import Biscuit


class BiscuitRecipe(models.Model):
    from apps.product.models.product import Product
    biscuit = models.ForeignKey(Biscuit, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    unit_of_measurement = models.CharField(default='kg', max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.biscuit)




