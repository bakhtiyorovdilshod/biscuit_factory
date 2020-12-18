from rest_framework.views import APIView
from rest_framework.response import Response

from api.biscuit.utils.price import calculate_biscuit_price, calculate_expense
from decimal import Decimal

from api.product.utils.price import calculate_man_product_price
from apps.biscuit.models import PriceList, Biscuit
from apps.product.models import ManufacturedProductPriceList, ManufacturedProduct


class CalculateProductPrice(APIView):
    def get(self, request):
        product_data = calculate_man_product_price()['data']
        if len(product_data)!=0:
            for i in product_data:
                price = 0
                product = i['product']
                from apps.product.utils.product import get_manufactured_product
                product = get_manufactured_product(product)
                total_price = i['total_price']
                quantity = i['quantity']
                total_price = Decimal(total_price)
                price = Decimal(total_price/Decimal(quantity))
                ManufacturedProductPriceList.objects.create(product=product, price=price)
            return Response({'status': 200})
        else:
            return Response({'error': 500})