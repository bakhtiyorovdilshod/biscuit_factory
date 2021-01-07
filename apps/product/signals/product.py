from django.db.models.signals import post_save
from django.dispatch import receiver
from api.warehouse.serializers.product import WareHouseProductCreateModelSerializer, \
    WareHouseManufacturedProductCreateModelSerializer
from apps.product.models import Product, ManufacturedProduct


@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    if created:
        product_data = {}
        product_data['product'] = instance.id
        warehouse_product = WareHouseProductCreateModelSerializer(data=product_data)
        warehouse_product.is_valid(raise_exception=True)
        warehouse_product.save()


@receiver(post_save, sender=ManufacturedProduct)
def create_manufactured_product(sender, instance, created, **kwargs):
    if created:
        product_data = {}
        product_data['manufactured_product'] = instance.id
        warehouse_product = WareHouseManufacturedProductCreateModelSerializer(data=product_data)
        warehouse_product.is_valid(raise_exception=True)
        warehouse_product.save()








