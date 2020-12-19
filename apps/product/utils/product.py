from api.product.serializers.add_product import ManufacturedProductAddListModelSerializer
from api.warehouse.serializers.add_product import ProductAddUpdateModelSerializer, ProductSubtractUpdateModelSerializer, \
    ManufacturedProductAddUpdateModelSerializer
from apps.biscuit.utils.biscuit import get_warehouse_product, get_product_price, check_warehouse_product_quantity
from apps.product.models import AddProduct, ManufacturedProduct, ManufacturedProductPriceList, ProductPriceList
from apps.product.models.add_product import AddProductLog, AddManufacturedProductLog
from apps.recipe.models import ManufacturedProductRecipe
from apps.warehouse.models import WareHouseProduct, WareHouseManufacturedProduct
from decimal import Decimal
from rest_framework import serializers


def get_manufactured_product(product_id):
    try:
        return ManufacturedProduct.objects.get(id=product_id)
    except ManufacturedProduct.DoesNotExist:
        raise serializers.ValidationError('manufactured product not found')


def get_warehouse_manufactured_product(product):
    try:
        return WareHouseManufacturedProduct.objects.get(manufactured_product=product)
    except WareHouseManufacturedProduct.DoesNotExist:
        raise serializers.ValidationError('warehouse manufactured product not found')


def get_product_recipe(product):
    try:
        return ManufacturedProductRecipe.objects.filter(manufactured_product=product)
    except ManufacturedProductRecipe.DoesNotExist:
        raise serializers.ValidationError('product recipe not found')


def get_warehouse_manufactured_product_price(manufactured_product):
    try:
        return ManufacturedProductPriceList.objects.filter(product=manufactured_product).order_by('-id').first().price
    except AttributeError:
        raise serializers.ValidationError('product price  not found')


def add_product(instance):
    warehouse_product_data = {}
    total_price = instance.quantity * instance.price
    warehouse_product_data['quantity'] = Decimal(instance.quantity)
    product = get_warehouse_product(instance.product)
    warehouse_serializer = ProductAddUpdateModelSerializer(product, data=warehouse_product_data)
    warehouse_serializer.is_valid(raise_exception=True)
    warehouse_serializer.save()
    product.total_price += Decimal(total_price)
    product.set_average_price()
    product.save()
    ProductPriceList.objects.create(product=instance.product, price=Decimal(instance.price))


def add_product_log(instance):
    total_price = instance.quantity * instance.price
    total_price = Decimal(total_price)
    AddProductLog.objects.create(add_product_id=instance.id, product=instance.product, quantity=Decimal(instance.quantity),total_price=total_price)


def sub_product(instance):
    warehouse_product_data = {}
    obj = AddProductLog.objects.get(add_product_id=instance.id)
    warehouse_product_data['quantity'] = obj.quantity
    total_price = obj.quantity * obj.price
    product = get_warehouse_product(instance.product)
    warehouse_serializer = ProductSubtractUpdateModelSerializer(product, data=warehouse_product_data)
    warehouse_serializer.is_valid(raise_exception=True)
    warehouse_serializer.save()
    product.total_price -= Decimal(total_price)
    product.set_average_price()
    product.save()


def add_manufactured_product(instance):
    product = get_manufactured_product(instance.product.id)
    ware_product = get_warehouse_manufactured_product(product)
    recipe = get_product_recipe(product)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = Decimal(instance.quantity) * Decimal(value)
        new_total_price = Decimal(price) * quantity_value
        if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
            warehouse.quantity -= Decimal(quantity_value)
            warehouse.total_price -= Decimal(new_total_price)
            warehouse.save()
    if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
        ware_product.add_quantity(Decimal(instance.quantity))
        ware_product.set_total_price()
        ware_product.set_average_price()
        ware_product.save()
        return True
    else:
        return False


def subtract_manufactured_product(instance):
    obj = AddManufacturedProductLog.objects.get(manufactured_product_id=instance.id)
    product = get_manufactured_product(instance.product.id)
    ware_product = get_warehouse_manufactured_product(product)
    recipe = get_product_recipe(product)
    if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
        ware_product.subtract_quantity(obj.quantity)
        ware_product.set_total_price()
        ware_product.set_average_price()
        ware_product.save()
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
        if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
            warehouse.quantity -= new_quantity_value
            new_total_price = price * new_quantity_value
            warehouse.total_price -= new_total_price
            warehouse.save()
    if check_warehouse_product_quantity(recipe, instance.quantity) == len(recipe):
        ware_product.add_quantity(instance.quantity)
        ware_product.set_total_price()
        ware_product.set_average_price()
        ware_product.save()
        obj.quantity = instance.quantity
        obj.product = instance.product
        obj.save()


def add_manufactured_product_log(instance):
    AddManufacturedProductLog.objects.create(manufactured_product_id=instance.id, product=instance.product, quantity=instance.quantity)