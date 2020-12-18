from rest_framework import serializers

from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.client.serializers.client import ClientModelSerializer
from apps.biscuit.models.sale import BuyingBiscuit, SaleBiscuitPrice
from rest_framework.serializers import ValidationError


class SaleBiscuitModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingBiscuit
        fields = "__all__"

    def create(self, validated_data):
        biscuit = validated_data.get('biscuit')
        quantity = validated_data.get('quantity')
        comment = validated_data.get('comment')
        payment_type = validated_data.get('payment_type')
        client = validated_data.get('client')
        from apps.biscuit.utils.sale import check_warehouse_biscuit_quantity
        from apps.biscuit.utils.biscuit import get_warehouse_biscuit
        ware_biscuit = get_warehouse_biscuit(biscuit)
        if check_warehouse_biscuit_quantity(ware_biscuit, quantity):
            instance = BuyingBiscuit.objects.create(biscuit=biscuit, quantity=quantity, comment=comment, payment_type=payment_type, client=client)
            return instance
        else:
            raise ValidationError('not enough biscuits in warehouse')

    def update(self, instance, validated_data):
        biscuit = validated_data.get('biscuit')
        quantity = validated_data.get('quantity')
        from apps.biscuit.utils.sale import check_warehouse_biscuit_quantity
        from apps.biscuit.utils.biscuit import get_warehouse_biscuit
        ware_biscuit = get_warehouse_biscuit(biscuit)
        if check_warehouse_biscuit_quantity(ware_biscuit, quantity):
            instance.biscuit = validated_data.get('biscuit', instance.biscuit)
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.comment = validated_data.get('comment', instance.comment)
            instance.payment_type = validated_data.get('payment_type', instance.payment_type)
            instance.client = validated_data.get('client', instance.client)
            instance.save()
            return instance
        else:
            raise ValidationError('not enougt products in warehouse')


class SaleBiscuitDetailModelSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)
    client = ClientModelSerializer(read_only=True, many=False)

    class Meta:
        model = BuyingBiscuit
        fields = [
            'id',
            'biscuit',
            'quantity',
            'currency',
            'total_price',
            'comment',
            'payment_type',
            'status',
            'client',
            'created_date',
            'modified_date'
        ]


class SaleBiscuitPriceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleBiscuitPrice
        fields = [
            'biscuit',
            'sale_price',
            'default_price'
        ]


class SaleBiscuitPriceDetailModelSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = SaleBiscuitPrice
        fields = [
            'biscuit',
            'sale_price',
            'default_price',
            'created_date',
            'modified_date'
        ]