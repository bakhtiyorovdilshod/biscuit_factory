from rest_framework.views import APIView

from api.staff.serializers.salary import StaffSalaryModelSerializer, StaffSalaryDetailModelSerializer
from apps.staff.models import StaffSalary
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.user.models import Account


class WareHouseStaffSalaryListAPIView(APIView):

    def get_account(self, staff_id):
        try:
            return Account.objects.get(user=staff_id)
        except Account.DoesNotExist:
            raise ValidationError('staff not found')

    def get(self, request):
        staff_id = request.query_params.get('staff_id')
        account = self.get_account(staff_id)
        queryset = StaffSalary.objects.filter(staff=account)
        serializer = StaffSalaryDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class WareHouseStaffSalaryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return StaffSalary.objects.get(id=pk)
        except StaffSalary.DoesNotExist:
            raise ValidationError('object not found')

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = StaffSalaryDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        staff = self.get_object(pk)
        serializer = StaffSalaryModelSerializer(staff, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)