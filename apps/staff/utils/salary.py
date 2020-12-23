from decimal import Decimal

from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


def get_biscuit_price_for_staff(who):
    from apps.staff.models import SalaryQuantity
    try:
        salary_quantity = SalaryQuantity.objects.filter(for_who=who).order_by('-id').first()
        price = salary_quantity.cost
        quantity = salary_quantity.quantity
        cost = Decimal(price/quantity)
        return cost
    except AttributeError:
        raise ValidationError('biscuit price list not found')


def check_biscuit_price_for_staff(who):
    from apps.staff.models import SalaryQuantity
    salary_quantity = SalaryQuantity.objects.filter(for_who=who)
    if salary_quantity.exists():
        return True
    else:
        return False


def get_staff_user(staff_id):
    try:
        return User.objects.get(id=staff_id).id
    except AttributeError:
        raise ValidationError('staff not found')
