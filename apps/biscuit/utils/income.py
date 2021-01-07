from apps.biscuit.models import SaleBiscuitPrice, IncomeBiscuit
from decimal import Decimal

from apps.warehouse.models import Income, ReserveMoney
from django.http import Http404
from rest_framework import serializers


def get_biscuit_cost(biscuit):
    try:
        return SaleBiscuitPrice.objects.filter(biscuit=biscuit).order_by('-id').first().default_price
    except SaleBiscuitPrice.DoesNotExist:
        raise serializers.ValidationError('sale biscuit price not found')


def get_reserve_money(pk):
    try:
        return ReserveMoney.objects.get(pk=pk)
    except ReserveMoney.DoesNotExist:
        raise serializers.ValidationError(' reserve money not found')

def get_income(pk):
    try:
        return Income.objects.get(pk=pk)
    except Income.DoesNotExist:
        raise serializers.ValidationError('income not found')


def biscuit_income(instance):
    total_price = instance.total_price
    quantity = instance.quantity
    cost = get_biscuit_cost(instance.biscuit)
    total_income = Decimal(total_price - (quantity * cost))
    for_one_biscuit_income = Decimal(total_income/quantity)
    IncomeBiscuit.objects.create(income=for_one_biscuit_income, biscuit=instance.biscuit)
    obj = get_icome(1)
    reserve = get_reserve_money(1)
    percentage = reserve.percentage
    reserve.total_price = reserve.total_price + Decimal((percentage*for_one_biscuit_income/Decimal(100)))
    obj.total_price = obj.total_price + total_income
    obj.save()
    reserve.save()