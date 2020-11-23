from django.db import models
import datetime


class Biscuit(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    unit_of_measurement = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
