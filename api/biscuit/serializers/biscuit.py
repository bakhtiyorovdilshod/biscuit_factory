from rest_framework.serializers import ModelSerializer

from apps.biscuit.models import SaleBiscuitPrice, BuyingBiscuit
from apps.biscuit.models.biscuit import Biscuit, PriceList, ReturnBiscuit
from decimal import Decimal

from apps.biscuit.utils.biscuit import get_biscuit
from apps.warehouse.models import WareHouseBiscuit


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
        price = validated_data.pop('price')
        biscuit, _ = Biscuit.objects.get_or_create(name=name, price=price, **validated_data)
        PriceList.objects.create(biscuit=biscuit, price=price)
        return biscuit

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        obj = PriceList.objects.filter(biscuit__id=instance.id).first()
        obj.price = validated_data.get('price', instance.price)
        obj.save()
        return instance


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


class ReturnDetailBiscuitCostSerializer(ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = ReturnBiscuit
        fields = [
            'id',
            'biscuit',
            'comment',
            'quantity',
            'created_date',
            'modified_date'
        ]


class ReturnBiscuitSerializer(ModelSerializer):
    class Meta:
        model = ReturnBiscuit
        fields = "__all__"

    def create(self, validated_data):
        biscuit = validated_data['biscuit']
        # biscuit = get_biscuit(biscuit).id
        quantity = validated_data['quantity']
        comment = validated_data['comment']
        ware_house_biscuit = WareHouseBiscuit.objects.filter(biscuit=biscuit).first()
        ware_house_biscuit.add_quantity(Decimal(quantity))
        ware_house_biscuit.set_total_price()
        ware_house_biscuit.set_average_price()
        ware_house_biscuit.save()
        instance = ReturnBiscuit.objects.create(biscuit=biscuit, quantity=quantity, comment=comment)
        return instance
