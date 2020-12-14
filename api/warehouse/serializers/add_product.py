from rest_framework.serializers import ModelSerializer
from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct


class ProductAddUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = WareHouseProduct
        fields = [
            'quantity'
        ]

    def update(self, instance, validated_data):
        instance.quantity += validated_data.get('quantity', instance.quantity)
        return instance


class ProductSubtractUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = WareHouseProduct
        fields = [
            'quantity'
        ]

    def update(self, instance, validated_data):
        instance.quantity = instance.quantity - validated_data.get('quantity', instance.quantity)
        return instance


class ProductFullUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = WareHouseProduct
        fields = [
            'product',
            'quantity'
        ]


class ManufacturedProductAddUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = WareHouseManufacturedProduct
        fields = [
            'quantity'
        ]

    def update(self, instance, validated_data):
        instance.quantity += validated_data.get('quantity', instance.quantity)
        return instance