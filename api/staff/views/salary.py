from rest_framework import viewsets

from api.staff.serializers.salary import SalaryPercentageModelSerializer, StaffSalaryModelSerializer
from apps.staff.models import SalaryPercentage, StaffSalary


class SalaryPercentageModelViewSet(viewsets.ModelViewSet):
    queryset = SalaryPercentage.objects.all()
    serializer_class = SalaryPercentageModelSerializer


class StaffSalaryModelSerializerModelViewSet(viewsets.ModelViewSet):
    queryset = StaffSalary.objects.all()
    serializer_class = StaffSalaryModelSerializer





