from rest_framework import serializers
from apps.warehouse.models.income import TakeMoney, Income, ReserveMoney


class TakeMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeMoney
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class ReserveMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveMoney
        fields = "__all__"
