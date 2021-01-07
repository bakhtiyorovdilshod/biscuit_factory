from rest_framework import serializers

from api.warehouse.utils.income import subtract_money, subtract_money_update
from apps.warehouse.models.income import TakeMoney, Income, ReserveMoney
from rest_framework.serializers import ValidationError


class TakeMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeMoney
        fields = "__all__"

    def validate(self, attrs):
        if not attrs.get('price'):
            raise ValidationError({'error': 'price not found'})

        if not attrs.get('comment'):
            raise ValidationError({'error': 'comment not found'})
        return attrs

    def create(self, validated_data):
        price = validated_data.get('price')
        comment = validated_data.get('comment')
        instance = TakeMoney.objects.create(price=price, comment=comment)
        subtract_money(validated_data)
        return instance

    def update(self, instance, validated_data):
        subtract_money_update(instance, validated_data)
        instance.price = validated_data.get('price', instance.price)
        instance.comment = validated_data.get('quantity', instance.comment)
        instance.save()
        return instance


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class ReserveMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveMoney
        fields = "__all__"
