from apps.biscuit.models import Biscuit, BuyingBiscuitLog
from apps.warehouse.models import WareHouseBiscuit


def sale_biscuit(instance):
    ware_biscuit = WareHouseBiscuit.objects.get(biscuit=instance.biscuit)
    ware_biscuit.subtract_quantity(instance.quantity)
    ware_biscuit.set_total_price()
    ware_biscuit.set_average_price()
    ware_biscuit.save()


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
    ware_biscuit = WareHouseBiscuit.objects.get(biscuit=instance.biscuit)
    ware_biscuit.add_quantity(obj.quantity)
    ware_biscuit.subtract_quantity(instance.quantity)
    ware_biscuit.set_total_price()
    ware_biscuit.set_average_price()
    ware_biscuit.save()
    obj.quantity = instance.quantity
    obj.biscuit = instance.biscuit
    obj.save()