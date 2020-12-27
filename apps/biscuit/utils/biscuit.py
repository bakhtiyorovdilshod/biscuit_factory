from api.product.serializers.sub_product import SubProductModelSerializer
from apps.biscuit.models import Biscuit, ProduceBiscuitLog, PriceList
from apps.product.models import AddProduct, ProductPriceList, SubProduct
from apps.recipe.models import BiscuitRecipe

from django.http import Http404
from rest_framework import serializers
from decimal import Decimal


def get_warehouse_product(product):
    from apps.warehouse.models import WareHouseBiscuit, WareHouseProduct
    try:
        return WareHouseProduct.objects.get(product=product)
    except WareHouseProduct.DoesNotExist:
        raise serializers.ValidationError('warehouse product not found')


def get_product_price(product):
    try:
        return ProductPriceList.objects.filter(product=product).order_by('-id').first().price
    except AttributeError:
        raise serializers.ValidationError('product price list not found')


def get_biscuit_price(biscuit):
    try:
        return PriceList.objects.filter(biscuit=biscuit).order_by('-id').first().price
    except AttributeError:
        raise serializers.ValidationError('biscuit price list not found')


def get_warehouse_biscuit(biscuit):
    from apps.warehouse.models import WareHouseBiscuit
    try:
        return WareHouseBiscuit.objects.get(biscuit=biscuit)
    except WareHouseBiscuit.DoesNotExist:
        raise serializers.ValidationError('warehouse biscuit not found')


def get_biscuit(pk):
    try:
        return Biscuit.objects.get(id=pk)
    except Biscuit.DoesNotExist:
        raise serializers.ValidationError('biscuit not found')


def get_biscuit_recipe(biscuit):
    try:
        return BiscuitRecipe.objects.filter(biscuit=biscuit)
    except BiscuitRecipe.DoesNotExist:
        raise serializers.ValidationError('biscuit recipe not found')


def check_warehouse_product_quantity(recipes, quantity):
    k = 0
    for recipe in recipes:
        product = recipe.product
        value = recipe.value
        warehouse = get_warehouse_product(product)
        quantity_value = Decimal(quantity * value)
        if warehouse.quantity > quantity_value:
            k = k + 1
    return k


def add_product(instance):
    biscuit = get_biscuit(instance.biscuit.id)
    ware_biscuit = get_warehouse_biscuit(biscuit)
    recipe = get_biscuit_recipe(biscuit)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = instance.quantity * value
        new_total_price = price * quantity_value
        if check_warehouse_product_quantity(recipe, instance.quantity)==len(recipe):
            warehouse.quantity -= quantity_value
            warehouse.total_price -= new_total_price
            warehouse.save()
            data ={}
            data['log_id'] = instance.id
            data['product'] = product.id
            data['quantity'] = quantity_value
            data['price'] = price
            data['total_price'] = new_total_price
            serializer = SubProductModelSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
    if check_warehouse_product_quantity(recipe, instance.quantity)==len(recipe):
        ware_biscuit.add_quantity(instance.quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.save()
        return True
    else:
        return False


def sub_product(instance):
    obj = ProduceBiscuitLog.objects.get(produce_biscuit_id=instance.id)
    biscuit = get_biscuit(obj.biscuit.id)
    recipe = get_biscuit_recipe(biscuit)
    ware_biscuit = get_warehouse_biscuit(biscuit)
    data = {}
    data['product'] = instance.product
    data['quantity'] = instance.quantity
    data['total_price'] = get_product_price(instance.product) * instance.quantity
    sub_obj = SubProduct.objects.filter(log_id=instance.id)
    serializer = SubProductModelSerializer(sub_obj, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
        ware_biscuit.subtract_quantity(obj.quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.save()
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
        new_total_price = price * new_quantity_value
        if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
            warehouse.quantity -= new_quantity_value
            warehouse.total_price -= new_total_price
            warehouse.save()
    if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
        ware_biscuit.add_quantity(instance.quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.save()
        obj.quantity = instance.quantity
        obj.biscuit = instance.biscuit
        obj.save()


def create_produce_log(instance):
    ProduceBiscuitLog.objects.create(produce_biscuit_id=instance.id, biscuit=instance.biscuit, quantity=instance.quantity, status=instance.status)



