from rest_framework import serializers

from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.client.serializers.client import ClientModelSerializer
from apps.biscuit.models.sale import BuyingBiscuit


class SaleBiscuitModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingBiscuit
        fields = "__all__"


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