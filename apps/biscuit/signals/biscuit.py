from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.serializers import ValidationError

from api.warehouse.serializers.biscuit import WareHouseBiscuitCreateModelSerializer
from apps.biscuit.models import Biscuit, UnfitBiscuit, BuyingBiscuit
from apps.biscuit.models.produce import ProduceBiscuit
from apps.biscuit.utils.biscuit import add_product, sub_product, create_produce_log
from apps.biscuit.utils.income import biscuit_income
from apps.biscuit.utils.sale import sale_biscuit, sale_biscuit_log, change_sale_biscuit
from apps.biscuit.utils.unfit_biscuit import add_quantity_unfit_biscuit, create_unfit_biscuit_log, \
    subtract_quantity_unfit_biscuit


@receiver(post_save, sender=ProduceBiscuit)
def produce_biscuit(sender, instance, created, **kwargs):
    if created:
        if add_product(instance):
            create_produce_log(instance)
    if not created:
        sub_product(instance)



@receiver(post_save, sender=Biscuit)
def create_biscuit(sender, instance, created, **kwargs):
    if created:
        data= {}
        data['biscuit'] = instance.id
        warehouse_biscuit = WareHouseBiscuitCreateModelSerializer(data=data)
        warehouse_biscuit.is_valid(raise_exception=True)
        warehouse_biscuit.save()


@receiver(post_save, sender=UnfitBiscuit)
def create_unfit_biscuit(sender, instance, created, **kwargs):
    if created:
        add_quantity_unfit_biscuit(instance)
        create_unfit_biscuit_log(instance)
    if not created:
        subtract_quantity_unfit_biscuit(instance)


@receiver(post_save, sender=BuyingBiscuit)
def sale_biscuit_to_company(sender, instance, created, **kwargs):
    if created:
        if sale_biscuit(instance):
            sale_biscuit_log(instance)
    if not created:
        change_sale_biscuit(instance)
        if instance.delivery_status[2][0]=='delivered':
            biscuit_income(instance)






