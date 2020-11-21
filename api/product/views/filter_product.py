from rest_framework.views import APIView
from rest_framework.response import Response
from apps.product.models.add_product import AddProduct
from api.product.serializers.add_product import ProductAddDetailModelSerializer


class ProductHistoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        date_one = request.query_params.get('date_one', None)
        date_two = request.query_params.get('date_two', None)
        if date_two is None:
            products = AddProduct.objects.filter(created_date__date=date_one)
        elif date_one is None:
            products = AddProduct.objects.filter(created_date__date=date_two)
        else:
            products = AddProduct.objects.filter(created_date__date__range=[date_one, date_two])
        serializer = ProductAddDetailModelSerializer(products, many=True)
        return Response(serializer.data)
