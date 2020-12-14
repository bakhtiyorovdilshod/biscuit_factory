from django.db.models.signals import post_save
from django.dispatch import receiver

from api.warehouse.serializers.add_product import ProductAddUpdateModelSerializer, ProductSubtractUpdateModelSerializer
from api.warehouse.serializers.product import WareHouseProductCreateModelSerializer, \
    WareHouseManufacturedProductCreateModelSerializer
from apps.product.models import Product, ManufacturedProduct, AddProduct, AddManufacturedProduct
from apps.product.utils.product import add_product, sub_product, add_product_log, add_manufactured_product_log, \
    add_manufactured_product, subtract_manufactured_product
from apps.warehouse.models import WareHouseProduct


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


@receiver(post_save, sender=AddProduct)
def product_add_quantity(sender, instance, created, **kwargs):
    if created:
        add_product(instance)
        add_product_log(instance)
    if not created:
        sub_product(instance)
        add_product(instance)


@receiver(post_save, sender=AddManufacturedProduct)
def manufactured_product_add_quantity(sender, instance, created, **kwargs):
    if created:
        add_manufactured_product(instance)
        add_manufactured_product_log(instance)
    if not created:
        subtract_manufactured_product(instance)



