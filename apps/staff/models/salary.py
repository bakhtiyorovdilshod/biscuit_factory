from django.db import models
import decimal

from apps.user.models import Account


class SalaryPercentage(models.Model):
    percentage = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.percentage)


class StaffSalary(models.Model):
    salary_status = (
        ('not_given', 'not_given'),
        ('given', 'given')
    )
    staff = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    status = models.CharField(max_digits=20, choices=salary_status, default='not_given')

    def __str(self):
        return str(self.staff)
