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

    def update(self, instance, validated_data):
        instance.biscuit = validated_data.get('biscuit', instance.biscuit)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


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
