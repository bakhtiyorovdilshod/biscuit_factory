from rest_framework.serializers import ModelSerializer
from apps.expense.models.expense import Expense, QuantityExpense


class ExpenseModelSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"


class QuantityExpenseModelSerializer(ModelSerializer):
    class Meta:
        model = QuantityExpense
        fields = [
            'expense',
            'cost'
        ]


class QuantityExpenseDetailModelSerializer(ModelSerializer):
    expense = ExpenseModelSerializer(read_only=True, many=False)

    class Meta:
        model = QuantityExpense
        fields = [
            'expense',
            'cost',
            'currency',
            'created_date',
            'modified_date'
        ]