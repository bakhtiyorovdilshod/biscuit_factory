from decimal import Decimal

from api.user.serializers.user import AccountSerializer
from apps.staff.models import SalaryQuantity, StaffSalary, StaffBiscuit, TechnologicalSalary
from rest_framework.serializers import ModelSerializer

from apps.staff.utils.salary import get_staff_user, check_biscuit_price_for_staff
from rest_framework.serializers import ValidationError


class SalaryPercentageModelSerializer(ModelSerializer):
    class Meta:
        model = SalaryQuantity
        fields = "__all__"


class StaffSalaryModelSerializer(ModelSerializer):
    class Meta:
        model = StaffSalary
        fields = "__all__"


class StaffSalaryDetailModelSerializer(ModelSerializer):
    staff = AccountSerializer(read_only=True, many=False)

    class Meta:
        model = StaffSalary
        fields = [
            'id',
            'staff',
            'biscuit_quantity',
            'salary',
            'status',
            'created_date',
            'modified_date'
        ]


class StaffBiscuitSerializer(ModelSerializer):
    class Meta:
        model = StaffBiscuit
        fields = "__all__"

    def validate(self, attrs):
        check_price = check_biscuit_price_for_staff('staff')
        if check_price == False:
            raise ValidationError('Ishchi xodimlar uchun pechene narxi topilmadi!')

    def create(self, validated_data):
        staff = validated_data['staff']
        biscuit_quantity = validated_data['biscuit_quantity']
        staff_salary = StaffSalary.objects.filter(staff=staff, status='not_given')
        if staff_salary.exists():
            staff_salary = staff_salary.first()
            staff_salary.add_quantity(Decimal(biscuit_quantity))
            staff_salary.set_total_price()
            staff_salary.save()
        else:
            staff_salary = StaffSalary.objects.create(staff=staff, status='not_given')
            staff_salary.add_quantity(Decimal(biscuit_quantity))
            staff_salary.set_total_price()
            staff_salary.save()
        instance = StaffBiscuit.objects.create(staff=staff, biscuit_quantity=biscuit_quantity, status='calculated')
        return instance

    def update(self, instance, validated_data):
        staff = validated_data['staff']
        biscuit_quantity = validated_data['biscuit_quantity']
        staff_salary = StaffSalary.objects.filter(staff=instance.staff, status='not_given').first()
        staff_salary.subtract_quantity(instance.biscuit_quantity)
        staff_salary.set_total_price()
        staff_salary.save()
        instance.staff = validated_data.get('staff', instance.staff)
        instance.biscuit_quantity = validated_data.get('biscuit_quantity', instance.biscuit_quantity)
        instance.save()
        staff_salary = StaffSalary.objects.filter(staff=staff, status='not_given').first()
        staff_salary.add_quantity(biscuit_quantity)
        staff_salary.set_total_price()
        staff_salary.save()
        return instance


class TechnologicalSalarySerializer(ModelSerializer):
    staff = AccountSerializer(read_only=True, many=False)
    
    class Meta:
        model = TechnologicalSalary
        fields = [
            'id',
            'staff',
            'biscuit_quantity',
            'salary',
            'status',
            'created_date',
            'modified_date'
        ]



