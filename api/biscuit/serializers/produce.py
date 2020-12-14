from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.user.serializers.user import AccountSerializer
from apps.biscuit.models import ProduceBiscuit
from rest_framework import serializers


class ProduceBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduceBiscuit
        fields = [
            'biscuit',
            'quantity',
            'staff',
            'total_price'
        ]


class ProduceBiscuitSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)
    staff = AccountSerializer(read_only=True, many=False)

    class Meta:
        model = ProduceBiscuit
        fields = [
            'id',
            'biscuit',
            'quantity',
            'staff',
            'total_price',
            'currency',
            'status',
            'created_date',
            'modified_date'
        ]


