from apps.biscuit.models import Biscuit, BuyingBiscuitLog
from apps.biscuit.utils.biscuit import get_warehouse_biscuit
from apps.warehouse.models import WareHouseBiscuit


def check_warehouse_biscuit_quantity(instance, quantity):
    if instance.quantity > quantity:
        return True
    else:
        return False


def sale_biscuit(instance):
    ware_biscuit = get_warehouse_biscuit(instance.biscuit)
    if check_warehouse_biscuit_quantity(ware_biscuit, instance.quantity):
        ware_biscuit.subtract_quantity(instance.quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.set_average_price()
        ware_biscuit.save()
        return True
    else:
        return False


def sale_biscuit_log(instance):
    BuyingBiscuitLog.objects.create(
        sale_id=instance.id,
        biscuit=instance.biscuit,
        quantity= instance.quantity,
        client=instance.client,
        payment_type= instance.payment_type,
        total_price = instance.total_price
    )


def change_sale_biscuit(instance):
    obj = BuyingBiscuitLog.objects.get(sale_id=instance.id)
    ware_biscuit = get_warehouse_biscuit(instance.biscuit)
    if check_warehouse_biscuit_quantity(ware_biscuit, instance.quantity):
        ware_biscuit.add_quantity(obj.quantity)
        ware_biscuit.subtract_quantity(instance.quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.set_average_price()
        ware_biscuit.save()
        obj.quantity = instance.quantity
        obj.biscuit = instance.biscuit
        obj.save()