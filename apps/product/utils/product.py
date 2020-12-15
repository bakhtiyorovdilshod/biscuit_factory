from api.product.serializers.add_product import ManufacturedProductAddListModelSerializer
from api.warehouse.serializers.add_product import ProductAddUpdateModelSerializer, ProductSubtractUpdateModelSerializer, \
    ManufacturedProductAddUpdateModelSerializer
from apps.product.models import AddProduct, ManufacturedProduct, ManufacturedProductPriceList, ProductPriceList
from apps.product.models.add_product import AddProductLog, AddManufacturedProductLog
from apps.recipe.models import ManufacturedProductRecipe
from apps.warehouse.models import WareHouseProduct, WareHouseManufacturedProduct
from decimal import Decimal


def add_product(instance):
    warehouse_product_data = {}
    total_price = instance.quantity * instance.price
    warehouse_product_data['quantity'] = Decimal(instance.quantity)
    product = WareHouseProduct.objects.get(product=instance.product)
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
    product = WareHouseProduct.objects.get(product=obj.product)
    warehouse_serializer = ProductSubtractUpdateModelSerializer(product, data=warehouse_product_data)
    warehouse_serializer.is_valid(raise_exception=True)
    warehouse_serializer.save()
    product.total_price -= Decimal(total_price)
    product.set_average_price()
    product.save()


def add_manufactured_product(instance):
    product = ManufacturedProduct.objects.get(id=instance.product.id)
    ware_product = WareHouseManufacturedProduct.objects.get(manufactured_product=product)
    recipe = ManufacturedProductRecipe.objects.filter(manufactured_product=product)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = WareHouseProduct.objects.get(product=product)
        price = ProductPriceList.objects.filter(product=product).order_by('-id').first().price
        quantity_value = Decimal(instance.quantity) * Decimal(value)
        warehouse.quantity -= Decimal(quantity_value)
        new_total_price = Decimal(price) * quantity_value
        warehouse.total_price -= Decimal(new_total_price)
        warehouse.save()
    ware_product.add_quantity(Decimal(instance.quantity))
    ware_product.set_total_price()
    ware_product.set_average_price()
    ware_product.save()


def subtract_manufactured_product(instance):
    obj = AddManufacturedProductLog.objects.get(manufactured_product_id=instance.id)
    product = ManufacturedProduct.objects.get(id=instance.product.id)
    ware_product = WareHouseManufacturedProduct.objects.get(manufactured_product=product)
    recipe = ManufacturedProductRecipe.objects.filter(manufactured_product=product)
    ware_product.subtract_quantity(obj.quantity)
    ware_product.set_total_price()
    ware_product.set_average_price()
    ware_product.save()
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = WareHouseProduct.objects.get(product=product)
        price = ProductPriceList.objects.filter(product=product).order_by('-id').first().price
        quantity_value = obj.quantity * value
        warehouse.quantity += quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price += new_total_price
        new_quantity_value = instance.quantity * value
        warehouse.quantity -= new_quantity_value
        new_total_price = price * new_quantity_value
        warehouse.total_price -= new_total_price
        warehouse.save()
    ware_product.add_quantity(instance.quantity)
    ware_product.set_total_price()
    ware_product.set_average_price()
    ware_product.save()
    obj.quantity = instance.quantity
    obj.product = instance.product
    obj.save()


def add_manufactured_product_log(instance):
    AddManufacturedProductLog.objects.create(manufactured_product_id=instance.id, product=instance.product, quantity=instance.quantity)