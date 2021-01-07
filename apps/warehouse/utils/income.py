from apps.biscuit.utils.income import get_income
from apps.warehouse.models import TakeMoney, Income, TakeMoneyLog


def sub_money(instance):
    price = instance.price
    income = get_income(1)
    income.total_price -= price
    income.save()
    TakeMoneyLog.objects.create(take_money_log_id=instance.id, price=instance.price, comment=instance.comment)


def edit_sub_money(instance):
    obj = TakeMoneyLog.objects.get(take_money_log_id=instance.id)
    old_price = obj.price
    income = get_income(1)
    income.total_price += old_price
    income.total_price -= instance.price
    income.save()
    obj.price = instance.price
    obj.comment = instance.comment
    obj.save()