from django.db import models


class Expense(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class QuantityExpense(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=10, default='So\'m')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.expense)