from rest_framework.views import APIView
from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct
from apps.warehouse.models.biscuit import WareHouseBiscuit
from api.warehouse.serializers.product import WareHouseProductDetailModelSerializer, WareHouseManufacturedProductDetailModelSerializer
from api.warehouse.serializers.biscuit import WareHouseBiscuitDetailModelSerializer
from rest_framework.response import Response


class WareHouseProductsAPIView(APIView):
    def get(self, request):
        queryset = WareHouseProduct.objects.all()
        serializer = WareHouseProductDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class WareHouseBiscuitAPIView(APIView):
    def get(self, request):
        queryset = WareHouseBiscuit.objects.all()
        serializer = WareHouseBiscuitDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class WareHouseManufacturedProductAPIView(APIView):
    def get(self, request):
        queryset = WareHouseManufacturedProduct.objects.all()
        serializer = WareHouseManufacturedProductDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)
