from django.contrib import admin
from apps.expense.models.expense import *

admin.site.register(Expense)
admin.site.register(QuantityExpense)