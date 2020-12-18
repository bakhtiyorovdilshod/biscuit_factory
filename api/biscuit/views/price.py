from rest_framework.views import APIView
from rest_framework.response import Response

from api.biscuit.utils.price import calculate_biscuit_price, calculate_expense
from decimal import Decimal

from apps.biscuit.models import PriceList, Biscuit
from apps.biscuit.utils.biscuit import get_biscuit
from rest_framework.serializers import ValidationError


class CalculateBiscuitPrice(APIView):
    def get(self, request):
        biscuit_data = calculate_biscuit_price()['data']
        expense_total_price = calculate_expense()
        if len(biscuit_data)!=0:
            each_price_for_biscuit = Decimal(expense_total_price/len(biscuit_data))
            for i in biscuit_data:
                price = 0
                biscuit = i['biscuit']
                biscuit = get_biscuit(biscuit)
                total_price = i['total_price']
                quantity = i['quantity']
                total_price = Decimal(total_price) + Decimal(each_price_for_biscuit)
                price = Decimal(total_price/Decimal(quantity))
                PriceList.objects.create(biscuit=biscuit, price=price)
            return Response({'status': 200})
        else:
            raise ValidationError('do not have produced biscuits')


