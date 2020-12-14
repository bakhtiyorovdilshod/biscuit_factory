from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import Http404

from api.biscuit.serializers.produce import ProduceBiscuitSerializer, ProduceBiscuitCreateSerializer
from api.biscuit.utils.filter import AddBiscuitFilter
from apps.biscuit.models import ProduceBiscuit, Biscuit, PriceList
from apps.product.models import Product
from apps.recipe.models import BiscuitRecipe
from apps.warehouse.models import WareHouseBiscuit, WareHouseProduct
from rest_framework.response import Response


class ProduceBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = ProduceBiscuit.objects.all()
    serializer_class = ProduceBiscuitSerializer

    def get_object(self, pk):
        try:
            return ProduceBiscuit.objects.get(pk=pk)
        except ProduceBiscuit.DoesNotExist:
            raise Http404

    def create(self, request, *args, **kwargs):
        data = request.data
        price = PriceList.objects.filter(biscuit=data['biscuit']).order_by('-id').first().price
        data['total_price'] = data['quantity'] * price
        serializer = ProduceBiscuitCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data
        obj = self.get_object(pk)
        price = PriceList.objects.filter(biscuit=data['biscuit']).order_by('-id').first().price
        data['total_price'] = data['quantity'] * price
        serializer = ProduceBiscuitCreateSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FilterProduceBiscuit(ListAPIView):
    queryset = ProduceBiscuit.objects.all()
    serializer_class = ProduceBiscuitSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [AddBiscuitFilter]