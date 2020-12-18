from rest_framework import viewsets
from api.warehouse.serializers.income import TakeMoneySerializer, IncomeSerializer, ReserveMoneySerializer
from apps.warehouse.models.income import TakeMoney, Income, ReserveMoney
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.serializers import ValidationError


class TakeMoneyModelViewSet(viewsets.ModelViewSet):
    queryset = TakeMoney.objects.all()
    serializer_class = TakeMoneySerializer
    # permission_classes = (IsAuthenticated,)


class IncomeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            raise ValidationError('object not found')

    def get(self, request):
        queryset = self.get_object(1)
        serializer = IncomeSerializer(queryset, many=False)
        return Response(serializer.data)


class ReserveMoneyDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return ReserveMoney.objects.get(pk=1)
        except ReserveMoney.DoesNotExist:
            raise ValidationError('object not found')

    def get(self, request):
        queryset = self.get_object(1)
        serializer = ReserveMoneySerializer(queryset, many=False)
        return Response(serializer.data)

    def put(self, request):
        queryset = self.get_object(1)
        serializer = ReserveMoneySerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)







