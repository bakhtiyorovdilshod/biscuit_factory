from rest_framework.serializers import ModelSerializer
from apps.warehouse.models.product import WareHouseProduct


class ProductAddUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = WareHouseProduct
        fields = [
            'quantity'
        ]

    def update(self, instance, validated_data):
        instance.quantity += validated_data.get('quantity', instance.quantity)
        return instance


class ProductFullUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = WareHouseProduct
        fields = [
            'product',
            'quantity'
        ]