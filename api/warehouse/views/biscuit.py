from rest_framework.views import APIView
from apps.warehouse.models.biscuit import WareHouseBiscuit
from api.warehouse.serializers.biscuit import WareHouseBiscuitDetailModelSerializer
from rest_framework.response import Response


class WareHouseBiscuitAPIView(APIView):
    def get(self, request):
        queryset = WareHouseBiscuit.objects.all()
        serializer = WareHouseBiscuitDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)