from decimal import Decimal

from api.warehouse.serializers.add_product import ProductAddUpdateModelSerializer, ProductSubtractUpdateModelSerializer
from apps.biscuit.utils.biscuit import get_warehouse_product, get_product_price
from apps.product.models import ProductPriceList
from apps.product.utils.product import get_warehouse_manufactured_product, get_product_recipe


def add_product_to_warehouse(validated_data):
    warehouse_product_data = {}
    total_price = validated_data.get('quantity') * validated_data.get('price')
    warehouse_product_data['quantity'] = Decimal(validated_data.get('quantity'))
    product = validated_data.get('product')
    warehouse_serializer = ProductAddUpdateModelSerializer(product, data=warehouse_product_data)
    warehouse_serializer.is_valid(raise_exception=True)
    warehouse_serializer.save()
    product.total_price += Decimal(total_price)
    product.set_average_price()
    product.save()
    ProductPriceList.objects.create(product=product, price=Decimal(validated_data.get('price')))


def add_product_to_warehouse_update(instance, validated_data):
    warehouse_product_data = {}
    warehouse_product_data['quantity'] = instance.quantity
    total_price = instance.quantity * instance.price
    product = get_warehouse_product(instance.product)
    warehouse_serializer = ProductSubtractUpdateModelSerializer(product, data=warehouse_product_data)
    warehouse_serializer.is_valid(raise_exception=True)
    warehouse_serializer.save()
    product.total_price -= Decimal(total_price)
    product.set_average_price()
    product.save()
    add_product_to_warehouse(validated_data)


def manufactured_product_add(validated_data):
    product = validated_data.get('product')
    ware_product = get_warehouse_manufactured_product(product)
    recipe = get_product_recipe(product)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = Decimal(validated_data.get('quantity')) * Decimal(value)
        new_total_price = Decimal(price) * quantity_value
        warehouse.quantity -= Decimal(quantity_value)
        warehouse.total_price -= Decimal(new_total_price)
        warehouse.save()
    ware_product.add_quantity(Decimal(validated_data.get('quantity')))
    ware_product.set_total_price()
    ware_product.set_average_price()
    ware_product.save()


def manufactured_product_add_update(instance, validated_data):
    product = instance.product
    ware_product = get_warehouse_manufactured_product(product)
    recipe = get_product_recipe(product)
    ware_product.subtract_quantity(instance.quantity)
    ware_product.set_total_price()
    ware_product.set_average_price()
    ware_product.save()
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = get_warehouse_product(product)
        price = get_product_price(product)
        quantity_value = instance.quantity * value
        warehouse.quantity += quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price += new_total_price
        warehouse.save()
    manufactured_product_add(validated_data)






