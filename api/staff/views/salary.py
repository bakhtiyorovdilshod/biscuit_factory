from rest_framework import viewsets
from rest_framework.views import APIView

from api.staff.serializers.salary import SalaryPercentageModelSerializer, StaffSalaryModelSerializer, \
    StaffBiscuitSerializer
from apps.staff.models import SalaryQuantity, StaffSalary, StaffBiscuit
from apps.user.models import Account
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


class SalaryPercentageModelViewSet(viewsets.ModelViewSet):
    queryset = SalaryQuantity.objects.all()
    serializer_class = SalaryPercentageModelSerializer


class StaffBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = StaffBiscuit.objects.all()
    serializer_class = StaffBiscuitSerializer


class StaffSalaryListAPIView(APIView):

    def get_account(self, staff_id):
        try:
            return Account.objects.get(user=staff_id)
        except Account.DoesNotExist:
            raise ValidationError('staff not found')

    def get(self, request):
        account = self.get_account(request.user)
        queryset = StaffSalary.objects.filter(staff=account)
        serializer = StaffSalaryModelSerializer(queryset, many=True)
        return Response(serializer.data)


class StaffSalaryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return StaffSalary.objects.get(pk=pk)
        except StaffSalary.DoesNotExist:
            raise ValidationError('object not found')

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = StaffSalaryModelSerializer(queryset, many=False)
        return Response(serializer.data)

















