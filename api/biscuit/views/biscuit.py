from rest_framework import viewsets

from api.warehouse.serializers.biscuit import WareHouseBiscuitCreateModelSerializer
from apps.biscuit.models.biscuit import Biscuit
from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404


class BiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = Biscuit.objects.all()
    serializer_class = BiscuitModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Biscuit.objects.get(pk=pk)
        except Biscuit.DoesNotExist:
            raise Http404

    def create(self, request, *args, **kargs):
        data = request.data
        serializer = BiscuitModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        biscuit_id = serializer.data['id']
        biscuit_data = {}
        biscuit_data['biscuit'] = biscuit_id
        warehouse_biscuit = WareHouseBiscuitCreateModelSerializer(data=biscuit_data)
        warehouse_biscuit.is_valid(raise_exception=True)
        warehouse_biscuit.save()
        return Response(serializer.data)

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