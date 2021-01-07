from apps.biscuit.models import Biscuit, AddUnFitBiscuitLog
from apps.biscuit.utils.biscuit import get_biscuit_recipe, get_warehouse_product, get_product_price
from apps.product.models import ProductPriceList
from apps.recipe.models import BiscuitRecipe
from apps.warehouse.models import WareHouseUnfitBiscuit, WareHouseProduct
from rest_framework import serializers


def get_or_create_unfit_biscuit(biscuit, status):
    try:
        return WareHouseUnfitBiscuit.objects.get_or_create(biscuit=biscuit, status=status)
    except WareHouseProduct.DoesNotExist:
        raise serializers.ValidationError('warehouse product not found')


def add_quantity_unfit_biscuit(instance):
    unfit_biscuit, _ = get_or_create_unfit_biscuit(instance.biscuit, instance.status)
    recipe = get_biscuit_recipe(instance.biscuit)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = instance.quantity * value
        warehouse.quantity -= quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price -= new_total_price
        warehouse.save()
    unfit_biscuit.add_quantity(instance.quantity)
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()


def create_unfit_biscuit_log(instance):
    AddUnFitBiscuitLog.objects.create(unfit_biscuit_id=instance.id, biscuit=instance.biscuit, quantity=instance.quantity, status=instance.status)


def subtract_quantity_unfit_biscuit(instance):
    obj = AddUnFitBiscuitLog.objects.get(unfit_biscuit_id=instance.id)
    unfit_biscuit, _ = get_or_create_unfit_biscuit(instance.biscuit, instance.status)
    unfit_biscuit.subtract_quantity(obj.quantity)
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()
    recipe = get_biscuit_recipe(instance.biscuit)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = obj.quantity * value
        warehouse.quantity += quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price += new_total_price
        new_quantity_value = instance.quantity * value
        warehouse.quantity -= new_quantity_value
        new_total_price = price * new_quantity_value
        warehouse.total_price -= new_total_price
        warehouse.save()
    unfit_biscuit.add_quantity(instance.quantity)
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()
    obj.quantity = instance.quantity
    obj.save()