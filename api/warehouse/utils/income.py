from apps.biscuit.utils.income import get_income


def subtract_money(validated_data):
    price = validated_data.get('price')
    income = get_income(1)
    income.total_price -= price
    income.save()


def subtract_money_update(instance, validated_data):
    old_price = instance.price
    income = get_income(1)
    income.total_price += old_price
    income.save()
    subtract_money(validated_data)
