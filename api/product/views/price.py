from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.response import Response

from api.biscuit.utils.price import calculate_biscuit_price, calculate_expense
from decimal import Decimal

from api.product.utils.price import calculate_man_product_price, change_status_product
from apps.biscuit.models import PriceList, Biscuit
from apps.product.models import ManufacturedProductPriceList, ManufacturedProduct, AddManufacturedProduct


def find_the_same_product(data):
    my_dict = defaultdict(int)
    for i in data:
        my_dict[i['product']] += i['product_cost']
    my_list = [{'product': product, 'product_cost': product_cost} for product, product_cost in my_dict.items()]
    return my_list


class CalculateProductPrice(APIView):
    def get(self, request):
        from apps.product.utils.product import get_manufactured_product
        product_data = calculate_man_product_price()['data']
        product_data = find_the_same_product(product_data)
        if len(product_data)!=0:
            for i in product_data:
                price = 0
                product = i['product']
                print(product)
                product = get_manufactured_product(product)
                total_price = i['product_cost']
                number = AddManufacturedProduct.objects.filter(for_price='un_calculate', product=product)
                price = Decimal(total_price)/Decimal(len(number))
                ManufacturedProductPriceList.objects.create(product=product, price=price)
            change_status_product()
            return Response({'status': 200})
        else:
            return Response({'error': 500})