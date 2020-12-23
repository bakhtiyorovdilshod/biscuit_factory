from decimal import Decimal

from django.http import Http404

from apps.biscuit.models import PriceList, ProduceBiscuit, SaleBiscuitPrice
from apps.biscuit.utils.biscuit import get_product_price, get_biscuit_recipe
from apps.expense.models import QuantityExpense
from apps.product.models import ProductPriceList
from apps.recipe.models import BiscuitRecipe
from rest_framework.serializers import ValidationError
from collections import defaultdict

from apps.staff.models import StaffSalary, TechnologicalSalary


def get_biscuit_sale_price(biscuit):
    try:
        return SaleBiscuitPrice.objects.filter(biscuit=biscuit).order_by('-id').first().sale_price
    except AttributeError:
        raise ValidationError('biscuit sale price is not found!')


def change_status():
    produced_biscuits = ProduceBiscuit.objects.filter(for_price='un_calculate')
    for produced_biscuit in produced_biscuits:
        produced_biscuit.for_price = 'calculated'
        produced_biscuit.save()


def calculate_biscuit_price():
    data = {'data': [

    ]}
    produced_biscuits = ProduceBiscuit.objects.filter(for_price='un_calculate')
    each_price_for_biscuit = Decimal(calculate_expense() / len(produced_biscuits))
    staff_salary_for_biscuit = Decimal(staff_salary()/ len(produced_biscuits))
    technological_man_salary = Decimal(technological_salary()/len(produced_biscuits))
    for produced_biscuit in produced_biscuits:
        total_price = 0
        biscuit = produced_biscuit.biscuit
        quantity = produced_biscuit.quantity
        recipes = get_biscuit_recipe(biscuit)
        for recipe in recipes:
            product = recipe.product
            value = recipe.value
            product_price = get_product_price(product)
            total_price = Decimal(total_price + product_price * value * quantity + each_price_for_biscuit + staff_salary_for_biscuit + technological_man_salary)/Decimal(quantity)
        data['data'].append({
            'biscuit': biscuit.id,
            'biscuit_cost': total_price
        })
    return data


def calculate_expense():
    total_price = 0
    expenses = QuantityExpense.objects.filter(status='new')
    for expense in expenses:
        price = expense.cost
        total_price = total_price + price
        expense.status = 'completed'
        expense.save()
    return total_price


def staff_salary():
    total_price = 0
    staff_salaries = StaffSalary.objects.filter(status='not_given')
    for staff_salary in staff_salaries:
        price = staff_salary.salary
        total_price = total_price + price
        staff_salary.status = 'calculated'
        staff_salary.save()
    return total_price


def technological_salary():
    total_price = 0
    staff_salaries = TechnologicalSalary.objects.filter(status='not_given')
    for staff_salary in staff_salaries:
        price = staff_salary.salary
        total_price = total_price + price
        staff_salary.status = 'calculated'
        staff_salary.save()
    return total_price





