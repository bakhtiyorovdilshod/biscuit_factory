from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.warehouse.models import TakeMoney
from apps.warehouse.utils.income import sub_money, edit_sub_money


@receiver(post_save, sender=TakeMoney)
def take_money_from_income(sender, instance, created, **kwargs):
    if created:
        sub_money(instance)
    if not created:
        edit_sub_money(instance)