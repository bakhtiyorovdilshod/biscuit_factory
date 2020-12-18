from django.contrib import admin
from apps.staff.models.salary import SalaryPercentage, StaffSalary

admin.site.register(SalaryPercentage)
admin.site.register(StaffSalary)