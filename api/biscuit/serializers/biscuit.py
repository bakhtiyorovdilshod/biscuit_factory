from rest_framework.serializers import ModelSerializer
from apps.biscuit.models.biscuit import Biscuit, PriceList


class BiscuitModelSerializer(ModelSerializer):
    class Meta:
        model = Biscuit
        fields = "__all__"

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(BiscuitModelSerializer, self).run_validators(value)

    def create(self, validated_data):
        name = validated_data.pop('name')
        biscuit, _ = Biscuit.objects.get_or_create(name=name, **validated_data)
        return biscuit


class BiscuitCostSerializer(ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = PriceList
        fields = [
            'id',
            'biscuit',
            'price',
            'currency',
            'created_date',
            'modified_date'
        ]