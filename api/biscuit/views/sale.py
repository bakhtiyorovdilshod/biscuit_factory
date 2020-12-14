from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

from api.biscuit.serializers.sale import SaleBiscuitModelSerializer, SaleBiscuitDetailModelSerializer
from api.biscuit.utils.filter import SaleBiscuitFilter
from apps.biscuit.models import PriceList
from apps.biscuit.models.sale import BuyingBiscuit
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class SaleBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = BuyingBiscuit.objects.all()
    serializer_class = SaleBiscuitModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return BuyingBiscuit.objects.get(pk=pk)
        except BuyingBiscuit.DoesNotExist:
            raise Http404

    def create(self, request, *args, **kwargs):
        data = request.data
        price = PriceList.objects.filter(biscuit=data['biscuit']).order_by('-id').first().price
        data['total_price'] = data['quantity'] * price
        serializer = SaleBiscuitModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data
        obj = self.get_object(pk)
        price = PriceList.objects.filter(biscuit=data['biscuit']).order_by('-id').first().price
        data['total_price'] = data['quantity'] * price
        serializer = SaleBiscuitModelSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SaleBiscuitDetailModelSerializer(queryset, many=False)
        return Response(serializer.data)


class FilterSaleBiscuit(ListAPIView):
    queryset = BuyingBiscuit.objects.all()
    serializer_class = SaleBiscuitDetailModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SaleBiscuitFilter]
