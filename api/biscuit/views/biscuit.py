from rest_framework import viewsets

from api.warehouse.serializers.biscuit import WareHouseBiscuitCreateModelSerializer
from apps.biscuit.models.biscuit import Biscuit, PriceList, ReturnBiscuit
from api.biscuit.serializers.biscuit import BiscuitModelSerializer, ReturnBiscuitSerializer, \
    ReturnDetailBiscuitCostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from rest_framework.serializers import ValidationError


class BiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = Biscuit.objects.all()
    serializer_class = BiscuitModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Biscuit.objects.get(pk=pk)
        except Biscuit.DoesNotExist:
            raise ValidationError('pecheneni topilmadi!')

    def create(self, request, *args, **kargs):
        data = request.data
        serializer = BiscuitModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 200})

    def update(self, request, pk=None):
        biscuit = self.get_object(pk)
        serializer = BiscuitModelSerializer(biscuit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        biscuit = self.get_object(pk)
        serializer = BiscuitModelSerializer(biscuit, many=False)
        return Response(serializer.data)


class ReturnBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = ReturnBiscuit.objects.all()
    serializer_class = ReturnBiscuitSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = ReturnBiscuit.objects.all()
        serializer = ReturnDetailBiscuitCostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, *args, **kwargs):
        queryset = self.get_object()
        serializer = ReturnDetailBiscuitCostSerializer(queryset, many=False)
        return Response(serializer.data)