from rest_framework import serializers

from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from apps.order.models.order import ClientOrder


class ClientOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder
        fields = [
            'biscuit',
            'quantity',
            'comment',
            'status',
            'created_date',
            'modified_date'
        ]


class ClientOrderDetailModelSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = ClientOrder
        fields = [
            'id',
            'biscuit',
            'quantity',
            'comment',
            'status',
            'created_date',
            'modified_date'
        ]
