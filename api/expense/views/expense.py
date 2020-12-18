from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from api.expense.serializers.expense import ExpenseModelSerializer, QuantityExpenseModelSerializer, QuantityExpenseDetailModelSerializer
from apps.expense.models.expense import Expense, QuantityExpense
from rest_framework.serializers import ValidationError


class ExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseModelSerializer
    permission_classes = (IsAuthenticated,)


class QuantityExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = QuantityExpense.objects.all()
    serializer_class = QuantityExpenseModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return QuantityExpense.objects.get(pk=pk)
        except QuantityExpense.DoesNotExist:
            raise ValidationError('not found')

    def list(self, request):
        serializer = QuantityExpenseDetailModelSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = QuantityExpenseDetailModelSerializer(product, many=False)
        return Response(serializer.data)
