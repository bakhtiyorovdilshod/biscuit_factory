from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.biscuit.utils.biscuit import subtract_product, subtract_product_update
from api.staff.utils.salary import technological_salary, technological_salary_update
from api.user.serializers.user import AccountSerializer
from apps.biscuit.models import ProduceBiscuit
from rest_framework import serializers

from apps.biscuit.utils.biscuit import get_biscuit_recipe, check_warehouse_product_quantity, get_biscuit_price
from rest_framework.serializers import ValidationError

from apps.staff.utils.salary import check_biscuit_price_for_staff
from apps.user.models import Account


class ProduceBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduceBiscuit
        fields = [
            'biscuit',
            'quantity',
        ]

    def validate(self, attrs):
        if not attrs.get('biscuit'):
            raise ValidationError({'xatolik': 'pechene topilmadi'})

        if not attrs.get('quantity'):
            raise ValidationError({'xatolik': 'miqdori topilmadi'})
        recipes = get_biscuit_recipe(attrs.get('biscuit'))
        quantity = attrs.get('quantity')
        check_price = check_biscuit_price_for_staff('technological_man')
        if not Account.objects.filter(user__is_chief_technological_man=True).exists():
            raise ValidationError({'xatolik': 'bosh_texnologik_bol topilmadi'})
        if len(recipes) == 0:
            raise ValidationError({'error': 'Ushbu pecheneni retsepti kiritilmagan!'})
        if check_warehouse_product_quantity(recipes, quantity)!= len(recipes):
            raise ValidationError('Mahsulot yetarli emas!')
        if check_price == False:
            raise ValidationError('Bosh texnologikni pecheneni uchun ish haqqi kiritilmagan!')
        return attrs

    def create(self, validated_data):
        biscuit = validated_data.get('biscuit')
        quantity = validated_data.get('quantity')
        instance = ProduceBiscuit.objects.create(biscuit=biscuit, quantity=quantity)
        technological_salary(quantity)
        subtract_product(validated_data)
        return instance

    def update(self, instance, validated_data):
        biscuit = validated_data.get('biscuit')
        quantity = validated_data.get('quantity')
        technological_salary_update(instance, quantity)
        subtract_product_update(instance, validated_data)
        instance.biscuit = validated_data.get('biscuit', instance.biscuit)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance



class ProduceBiscuitSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)
    class Meta:
        model = ProduceBiscuit
        fields = [
            'id',
            'biscuit',
            'quantity',
            'currency',
            'status',
            'created_date',
            'modified_date'
        ]


