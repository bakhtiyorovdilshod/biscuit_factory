from rest_framework.views import APIView
from apps.warehouse.models.product import WareHouseProduct
from api.warehouse.serializers.product import WareHouseProductDetailModelSerializer
from rest_framework.response import Response


class WareHouseProductsAPIView(APIView):
    def get(self, request):
        queryset = WareHouseProduct.objects.all()
        serializer = WareHouseProductDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)