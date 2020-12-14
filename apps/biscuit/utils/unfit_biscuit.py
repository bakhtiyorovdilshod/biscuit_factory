from apps.biscuit.models import Biscuit, AddUnFitBiscuitLog
from apps.product.models import ProductPriceList
from apps.recipe.models import BiscuitRecipe
from apps.warehouse.models import WareHouseUnfitBiscuit, WareHouseProduct


def add_quantity_unfit_biscuit(instance):
    unfit_biscuit, _ = WareHouseUnfitBiscuit.objects.get_or_create(biscuit=instance.biscuit, status=instance.status)
    recipe = BiscuitRecipe.objects.filter(biscuit=instance.biscuit)
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
    unfit_biscuit.add_quantity(instance.quantity)
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()


def create_unfit_biscuit_log(instance):
    AddUnFitBiscuitLog.objects.create(unfit_biscuit_id=instance.id, biscuit=instance.biscuit, quantity=instance.quantity, status=instance.status)


def subtract_quantity_unfit_biscuit(instance):
    obj = AddUnFitBiscuitLog.objects.get(unfit_biscuit_id=instance.id)
    unfit_biscuit, _ = WareHouseUnfitBiscuit.objects.get_or_create(biscuit=instance.biscuit, status=instance.status)
    unfit_biscuit.subtract_quantity(obj.quantity)
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()
    recipe = BiscuitRecipe.objects.filter(biscuit=instance.biscuit)
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
    unfit_biscuit.add_quantity(instance.quantity)
    unfit_biscuit.set_total_price()
    unfit_biscuit.save()
    obj.quantity = instance.quantity
    obj.save()