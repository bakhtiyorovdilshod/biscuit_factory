from apps.staff.models import SalaryPercentage, StaffSalary
from rest_framework.serializers import ModelSerializer


class SalaryPercentageModelSerializer(ModelSerializer):
    class Meta:
        model = SalaryPercentage
        fields = "__all__"


class StaffSalaryModelSerializer(ModelSerializer):
    class Meta:
        model = StaffSalary
        fields = "__all__"
