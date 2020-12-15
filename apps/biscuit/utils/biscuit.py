from apps.biscuit.models import Biscuit, ProduceBiscuitLog, PriceList
from apps.product.models import AddProduct, ProductPriceList
from apps.recipe.models import BiscuitRecipe
from apps.warehouse.models import WareHouseBiscuit, WareHouseProduct


def add_product(instance):
    biscuit = Biscuit.objects.get(id=instance.biscuit.id)
    ware_biscuit = WareHouseBiscuit.objects.get(biscuit=biscuit)
    recipe = BiscuitRecipe.objects.filter(biscuit=biscuit)
    for i in recipe:
        product = i.product
        value = i.value
        warehouse = WareHouseProduct.objects.get(product=product)
        price = ProductPriceList.objects.filter(product=product).order_by('-id').first().price
        quantity_value = instance.quantity * value
        warehouse.quantity -= quantity_value
        new_total_price = price * quantity_value
        warehouse.total_price -= new_total_price
        warehouse.save()
    ware_biscuit.add_quantity(instance.quantity)
    ware_biscuit.set_total_price()
    ware_biscuit.save()


def sub_product(instance):
    obj = ProduceBiscuitLog.objects.get(produce_biscuit_id=instance.id)
    biscuit = Biscuit.objects.get(id=obj.biscuit.id)
    ware_biscuit = WareHouseBiscuit.objects.get(biscuit=biscuit)
    ware_biscuit.subtract_quantity(obj.quantity)
    ware_biscuit.set_total_price()
    ware_biscuit.save()
    recipe = BiscuitRecipe.objects.filter(biscuit=biscuit)
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
    ware_biscuit.add_quantity(instance.quantity)
    ware_biscuit.set_total_price()
    ware_biscuit.save()
    obj.quantity = instance.quantity
    obj.biscuit = instance.biscuit
    obj.save()


def create_produce_log(instance):
    ProduceBiscuitLog.objects.create(produce_biscuit_id=instance.id, biscuit=instance.biscuit, quantity=instance.quantity, status=instance.status)



