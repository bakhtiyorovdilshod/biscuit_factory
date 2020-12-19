from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.user.serializers.user import AccountSerializer
from apps.biscuit.models import ProduceBiscuit
from rest_framework import serializers

from apps.biscuit.utils.biscuit import get_biscuit_recipe, check_warehouse_product_quantity, get_biscuit_price
from rest_framework.serializers import ValidationError


class ProduceBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduceBiscuit
        fields = [
            'biscuit',
            'quantity',
            'staff',
        ]

    def create(self, validated_data):
        biscuit = validated_data.get('biscuit')
        quantity = validated_data.get('quantity')
        staff = validated_data.get('staff')
        recipes = get_biscuit_recipe(biscuit)
        price = get_biscuit_price(biscuit)
        if len(recipes)!=0:
            if check_warehouse_product_quantity(recipes, quantity) == len(recipes):
                instance = ProduceBiscuit.objects.create(biscuit=biscuit, quantity=quantity, staff=staff)
                return instance
            else:
                raise ValidationError('not enougt products in warehouse')
        else:
            raise ValidationError('This biscuit does not have recipe')

    def update(self, instance, validated_data):
        biscuit = validated_data.get('biscuit')
        quantity = validated_data.get('quantity')
        recipes = get_biscuit_recipe(biscuit)
        if len(recipes) != 0:
            if check_warehouse_product_quantity(recipes, quantity) == len(recipes):
                instance.biscuit = validated_data.get('biscuit', instance.biscuit)
                instance.quantity = validated_data.get('quantity', instance.quantity)
                instance.staff = validated_data.get('staff', instance.staff)
                instance.save()
                return instance
            else:
                raise ValidationError('not enougt products in warehouse')
        else:
            raise ValidationError('This biscuit does not have recipe')




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
            'currency',
            'status',
            'created_date',
            'modified_date'
        ]


