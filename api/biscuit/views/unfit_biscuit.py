from rest_framework import viewsets

from apps.biscuit.models import Biscuit
from apps.biscuit.models.unfit_biscuit import UnfitBiscuit
from api.biscuit.serializers.unfit_biscuit import *
from apps.warehouse.models import WareHouseUnfitBiscuit, WareHouseBiscuit
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.serializers import ValidationError


class UnFitBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = UnfitBiscuit.objects.all()
    serializer_class = UnfitBiscuitCreateSerializer

    def get_object(self, pk):
        try:
            return UnfitBiscuit.objects.get(pk=pk)
        except UnfitBiscuit.DoesNotExist:
            raise ValidationError('not found')

    def create(self, request):
        data = request.data
        serializer = UnfitBiscuitCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = UnfitBiscuitDetailSerializer(product)
        return Response(serializer.data)

    def list(self, request):
        products = UnfitBiscuit.objects.all()
        serializer = UnfitBiscuitDetailSerializer(products, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        product = self.get_object(pk)
        serializer = UnfitBiscuitCreateSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
