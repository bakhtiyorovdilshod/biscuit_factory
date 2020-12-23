from django.db import models
import decimal

from apps.staff.utils.salary import get_biscuit_price_for_staff
from apps.user.models import Account


class SalaryQuantity(models.Model):
    status = (
        ('staff', 'staff'),
        ('manager', 'manager'),
        ('technological_man', 'technological_man'),
    )
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(1))
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    for_who = models.CharField(max_length=50, choices=status, default='staff')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cost)


class StaffSalary(models.Model):
    salary_status = (
        ('not_given', 'not_given'),
        ('given', 'given'),
        ('calculated', 'calculated')
    )
    staff = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    biscuit_quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    status = models.CharField(max_length=20, choices=salary_status, default='not_given')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def add_quantity(self, value):
        self.biscuit_quantity += value

    def subtract_quantity(self, value):
        self.biscuit_quantity -= value

    def set_total_price(self):
        price = get_biscuit_price_for_staff('staff')
        self.salary = price * self.biscuit_quantity

    def __str__(self):
        return str(self.staff)


class StaffBiscuit(models.Model):
    salary_status = (
        ('un_calculate', 'un_calculate'),
        ('calculated', 'calculated')
    )
    staff = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    biscuit_quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    status = models.CharField(max_length=20, choices=salary_status, default='un_calculate')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.biscuit_quantity)


class TechnologicalSalary(models.Model):
    salary_status = (
        ('not_given', 'not_given'),
        ('given', 'given'),
        ('calculated', 'calculated')
    )
    staff = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    biscuit_quantity = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    status = models.CharField(max_length=20, choices=salary_status, default='not_given')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def add_quantity(self, value):
        self.biscuit_quantity += value

    def subtract_quantity(self, value):
        self.biscuit_quantity -= value

    def set_total_price(self):
        price = get_biscuit_price_for_staff('technological_man')
        self.salary = price * self.biscuit_quantity

    def __str__(self):
        return str(self.staff)




