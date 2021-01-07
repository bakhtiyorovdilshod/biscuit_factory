from rest_framework import serializers

from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.biscuit.utils.biscuit import unfit_biscuit_add_quantity, unfit_biscuit_subtract_quantity
from apps.biscuit.models import UnfitBiscuit
from apps.warehouse.models import WareHouseUnfitBiscuit
from rest_framework.serializers import ValidationError


class UnfitBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnfitBiscuit
        fields = [
            'biscuit',
            'quantity',
            'description',
            'status'
        ]

    def validate(self, attrs):
        if not attrs.get('biscuit'):
            raise ValidationError({'error': 'Biscuit not found'})
        if not attrs.get('quantity'):
            raise ValidationError({'error': 'quantity not found'})
        if not attrs.get('status'):
            raise ValidationError({'error': 'status not found'})
        if not attrs.get('description'):
            raise ValidationError({'error': 'description not found'})
        return attrs

    def create(self, validated_data):
        biscuit = validated_data.get('biscuit')
        status = validated_data.get('status')
        quantity = validated_data.get('quantity')
        description = validated_data.get('description')
        unfit_biscuit, _ = WareHouseUnfitBiscuit.objects.get_or_create(biscuit=biscuit, status=status)
        unfit_biscuit_add_quantity(validated_data, unfit_biscuit)
        instance = UnfitBiscuit.objects.create(biscuit=biscuit, quantity=quantity, description=description, status=status)
        return instance

    def update(self, instance, validated_data):
        unfit_biscuit_subtract_quantity(instance, validated_data)
        instance.biscuit = validated_data.get('biscuit', instance.biscuit)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.status = validated_data.get('status', instance.status)
        instance.description = validated_data.get('description', instance.quantity)
        instance.save()
        return instance


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
        ]

