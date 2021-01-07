from api.product.serializers.sub_product import SubProductModelSerializer
from apps.biscuit.utils.biscuit import get_biscuit, get_warehouse_biscuit, get_biscuit_recipe, get_warehouse_product, \
    get_product_price
from apps.biscuit.utils.income import biscuit_income
from apps.biscuit.utils.unfit_biscuit import get_or_create_unfit_biscuit


def subtract_product(validated_data):
    biscuit = validated_data.get('biscuit')
    ware_biscuit = get_warehouse_biscuit(biscuit)
    recipe = get_biscuit_recipe(biscuit)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = validated_data.get('quantity') * value
        new_total_price = price * quantity_value
        warehouse.quantity -= quantity_value
        warehouse.total_price -= new_total_price
        warehouse.save()
    ware_biscuit.add_quantity(validated_data.get('quantity'))
    ware_biscuit.set_total_price()
    ware_biscuit.save()


def subtract_product_update(instance, validated_data):
    biscuit = instance.biscuit
    old_recipe = get_biscuit_recipe(biscuit)
    ware_biscuit = get_warehouse_biscuit(biscuit)
    ware_biscuit.subtract_quantity(instance.quantity)
    ware_biscuit.set_total_price()
    ware_biscuit.save()
    for i in old_recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = instance.quantity * value
        warehouse.quantity += quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price += new_total_price
        warehouse.save()
    subtract_product(validated_data)


def unfit_biscuit_add_quantity(validated_data, unfit_biscuit):
    recipe = get_biscuit_recipe(validated_data.get('biscuit'))
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = validated_data.get('quantity') * value
        warehouse.quantity -= quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price -= new_total_price
        warehouse.save()
    unfit_biscuit.add_quantity(validated_data.get('quantity'))
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()


def unfit_biscuit_subtract_quantity(instance, validated_data):
    unfit_biscuit, _ = get_or_create_unfit_biscuit(instance.biscuit, instance.status)
    unfit_biscuit.subtract_quantity(instance.quantity)
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()
    old_recipe = get_biscuit_recipe(instance.biscuit)
    for i in old_recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = instance.quantity * value
        warehouse.quantity += quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price += new_total_price
        warehouse.save()
    unfit_biscuit, _ = get_or_create_unfit_biscuit(validated_data.get('biscuit'), validated_data.get('status'))
    unfit_biscuit_add_quantity(validated_data, unfit_biscuit)


def sale_biscuit_to_client(validated_data):
    ware_biscuit = get_warehouse_biscuit(validated_data.get('biscuit'))
    ware_biscuit.subtract_quantity(validated_data.get('quantity'))
    ware_biscuit.set_total_price()
    ware_biscuit.set_average_price()
    ware_biscuit.save()


def sale_biscuit_to_client_update(instance, validated_data):
    ware_biscuit = get_warehouse_biscuit(instance.biscuit)
    ware_biscuit.add_quantity(instance.quantity)
    ware_biscuit.set_total_price()
    ware_biscuit.set_average_price()
    ware_biscuit.save()
    if instance.delivery_status[2][0] == 'delivered':
        biscuit_income(instance)
    sale_biscuit_to_client(validated_data)