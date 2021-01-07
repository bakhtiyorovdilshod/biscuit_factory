from decimal import Decimal

from apps.staff.models import TechnologicalSalary
from apps.user.models import Account


def technological_salary(quantity):
    staff = Account.objects.filter(user__is_chief_technological_man=True).order_by('-id').first()
    staff_salary = TechnologicalSalary.objects.filter(staff=staff, status='not_given')
    if staff_salary.exists():
        staff_salary = staff_salary.first()
        staff_salary.add_quantity(Decimal(quantity))
        staff_salary.set_total_price()
        staff_salary.save()
    else:
        staff_salary = TechnologicalSalary.objects.create(staff=staff, status='not_given')
        staff_salary.add_quantity(Decimal(quantity))
        staff_salary.set_total_price()
        staff_salary.save()


def technological_salary_update(instance, new_quantity):
    staff_salary = TechnologicalSalary.objects.filter(status='not_given').first()
    staff_salary.subtract_quantity(instance.quantity)
    staff_salary.set_total_price()
    staff_salary.save()
    staff_salary.add_quantity(new_quantity)
    staff_salary.set_total_price()
    staff_salary.save()