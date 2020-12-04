from rest_framework import serializers

from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from apps.warehouse.models import WareHouseUnfitBiscuit


class WareHouseUnfitBiscuitSerailizer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(many=False, read_only=True)

    class Meta:
        model = WareHouseUnfitBiscuit
        fields = [
            "id",
            "biscuit",
            "quantity",
            "total_price",
            "created",
            "updated"
        ]