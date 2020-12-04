from rest_framework.views import APIView

from api.warehouse.serializers.unfit_biscuit import WareHouseUnfitBiscuitSerailizer
from apps.warehouse.models.unfit_biscuit import WareHouseUnfitBiscuit
from api.warehouse.serializers.biscuit import WareHouseBiscuitDetailModelSerializer
from rest_framework.response import Response


class WareHouseUnfitUnRecyclableBiscuitListAPIView(APIView):
    def get(self, request):
        queryset = WareHouseUnfitBiscuit.objects.filter(status='recyclable')
        serializer = WareHouseUnfitBiscuitSerailizer(queryset, many=True)
        return Response(serializer.data)


class WareHouseUnfitRecyclableBiscuitListAPIView(APIView):
    def get(self, request):
        queryset = WareHouseUnfitBiscuit.objects.filter(status='unrecyclable')
        serializer = WareHouseUnfitBiscuitSerailizer(queryset, many=True)
        return Response(serializer.data)