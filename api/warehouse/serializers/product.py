from rest_framework import serializers

from apps.product.models import ManufacturedProduct
from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct
from api.product.serializers.product import ProductModelSerializer, ManufacturedProductModelSerializer


class WareHouseProductCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseProduct
        fields = [
            'product'
        ]

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(WareHouseProductCreateModelSerializer, self).run_validators(value)

    def create(self, validated_data):
        product = validated_data.pop('product')
        product, _ = WareHouseProduct.objects.get_or_create(
            product=product, **validated_data)
        return product


class WareHouseProductDetailModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = WareHouseProduct
        fields = [
            'product',
            'quantity',
            'total_price',
            'average_price',
            'unit_of_measurement',
            'currency',
            'created_date'
        ]


class WareHouseManufacturedProductCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseManufacturedProduct
        fields = [
            'manufactured_product'
        ]

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(WareHouseManufacturedProductCreateModelSerializer, self).run_validators(value)

    def create(self, validated_data):
        product = validated_data.pop('manufactured_product')
        product, _ = WareHouseManufacturedProduct.objects.get_or_create(
            manufactured_product=product, **validated_data)
        return product


class WareHouseManufacturedProductDetailModelSerializer(serializers.ModelSerializer):
    manufactured_product = ManufacturedProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = WareHouseManufacturedProduct
        fields = [
            'manufactured_product',
            'quantity',
            'total_price',
            'average_price',
            'unit_of_measurement',
            'created_date'
        ]