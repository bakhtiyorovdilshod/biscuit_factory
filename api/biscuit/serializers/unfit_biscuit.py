from rest_framework import serializers

from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from apps.biscuit.models import UnfitBiscuit


class UnfitBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnfitBiscuit
        fields = [
            'biscuit',
            'quantity',
            'description',
            'status'
        ]


class UnfitBiscuitDetailSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = UnfitBiscuit
        fields = [
            'id',
            'biscuit',
            'quantity',
            'description',
            'total_price',
            'date'
        ]