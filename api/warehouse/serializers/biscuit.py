from rest_framework import serializers
from apps.warehouse.models.biscuit import WareHouseBiscuit
from api.biscuit.serializers.biscuit import BiscuitModelSerializer


class WareHouseBiscuitCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseBiscuit
        fields = [
            'biscuit'
        ]

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(WareHouseBiscuitCreateModelSerializer, self).run_validators(value)

    def create(self, validated_data):
        biscuit = validated_data.pop('biscuit')
        biscuit, _ = WareHouseBiscuit.objects.get_or_create(
            biscuit=biscuit, **validated_data)
        return biscuit


class WareHouseBiscuitDetailModelSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = WareHouseBiscuit
        fields = [
            'biscuit',
            'quantity',
            'total_price',
            'average_price',
            'unit_of_measurement',
            'currency',
            'created_date'
        ]