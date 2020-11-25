from django.db import models
from django.core.validators import RegexValidator


class Supplier(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    x_p = models.CharField(max_length=300, blank=True, null=True)
    m_f_o = models.CharField(max_length=300, blank=True, null=True)
    inn = models.CharField(max_length=300, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number is error")
    phone_number = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'