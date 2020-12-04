from rest_framework import viewsets

from apps.biscuit.models import Biscuit
from apps.biscuit.models.unfit_biscuit import UnfitBiscuit
from api.biscuit.serializers.unfit_biscuit import *
from apps.warehouse.models import WareHouseUnfitBiscuit, WareHouseBiscuit
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from django.http import Http404


class UnFitBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = UnfitBiscuit.objects.all()
    serializer_class = UnfitBiscuitCreateSerializer

    def get_object(self, pk):
        try:
            return UnfitBiscuit.objects.get(pk=pk)
        except UnfitBiscuit.DoesNotExist:
            raise Http404

    def create(self, request):
        data = request.data
        biscuit_id = data['biscuit']
        status = data['status']
        biscuit = Biscuit.objects.get(id=biscuit_id)
        serializer = UnfitBiscuitCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        obj = UnfitBiscuit.objects.get(id=serializer.save().id)
        obj.set_total_price()
        obj.save()
        instance, _ = WareHouseUnfitBiscuit.objects.get_or_create(biscuit=biscuit, status=status)
        instance.quantity = instance.quantity + data['quantity']
        instance.save()
        instance.set_total_price()
        instance.save()
        # ware_house_biscuit = WareHouseBiscuit.objects.get(biscuit=biscuit)
        # ware_house_biscuit.quantity = ware_house_biscuit.quantity - data['quantity']
        # ware_house_biscuit.set_total_price()
        # ware_house_biscuit.save()
        return Response(data=serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = UnfitBiscuitDetailSerializer(product)
        return Response(serializer.data)

    def list(self, request):
        products = UnfitBiscuit.objects.all()
        serializer = UnfitBiscuitDetailSerializer(products, many=True)
        return Response(serializer.data)

