from django.db import models
import decimal


class Income(models.Model):
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.total_price)


class ReserveMoney(models.Model):
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    percentage = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.total_price)


class TakeMoney(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.price


class TakeMoneyLog(models.Model):
    take_money_log_id = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=decimal.Decimal(0))
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.take_money_log_id
