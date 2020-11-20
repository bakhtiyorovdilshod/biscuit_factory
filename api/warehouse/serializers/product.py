from rest_framework import serializers
from apps.warehouse.models.product import WareHouseProduct


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