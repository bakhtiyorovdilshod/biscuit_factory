from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from apps.biscuit.models import ProduceBiscuit
from rest_framework import serializers


class ProduceBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduceBiscuit
        fields = [
            'id',
            'biscuit',
            'quantity',
            'staff'
        ]


class ProduceBiscuitSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = ProduceBiscuit
        fields = [
            'biscuit',
            'quantity',
            'date',
            'total_price'
        ]