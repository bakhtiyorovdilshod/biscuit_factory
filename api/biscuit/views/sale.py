from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

from api.biscuit.serializers.sale import SaleBiscuitModelSerializer, SaleBiscuitDetailModelSerializer, \
    SaleBiscuitPriceModelSerializer, SaleBiscuitPriceDetailModelSerializer
from api.biscuit.utils.filter import SaleBiscuitFilter
from api.biscuit.utils.price import get_biscuit_sale_price
from apps.biscuit.models import PriceList
from apps.biscuit.models.sale import BuyingBiscuit, SaleBiscuitPrice
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from apps.biscuit.utils.biscuit import get_biscuit_price


class SaleBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = BuyingBiscuit.objects.all()
    serializer_class = SaleBiscuitModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return BuyingBiscuit.objects.get(pk=pk)
        except BuyingBiscuit.DoesNotExist:
            raise ValidationError('not found')

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            biscuit = data['biscuit']
            quantity = data['quantity']
        except KeyError:
            raise ValidationError('biscuit or quantity not found')
        price = get_biscuit_sale_price(biscuit)
        data['total_price'] = quantity * price
        serializer = SaleBiscuitModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data
        try:
            biscuit = data['biscuit']
            quantity = data['quantity']
        except KeyError:
            raise ValidationError('biscuit or quantity not found')
        obj = self.get_object(pk)
        price = get_biscuit_sale_price(biscuit)
        data['total_price'] = quantity * price
        serializer = SaleBiscuitModelSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SaleBiscuitDetailModelSerializer(queryset, many=False)
        return Response(serializer.data)

    def list(self, request):
        queryset = BuyingBiscuit.objects.all()
        serializer = SaleBiscuitDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class FilterSaleBiscuit(ListAPIView):
    queryset = BuyingBiscuit.objects.all()
    serializer_class = SaleBiscuitDetailModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SaleBiscuitFilter]


class SaleBiscuitPriceAPIView(APIView):

    def get_object(self, pk):
        try:
            return SaleBiscuitPrice.objects.get(pk=pk)
        except SaleBiscuitPrice.DoesNotExist:
            raise ValidationError('not found')

    def post(self, request):
        data = request.data
        try:
            biscuit = data['biscuit']
        except KeyError:
            raise ValidationError('biscuit not found')
        default_price = get_biscuit_price(biscuit)
        data['default_price'] = default_price
        serializer = SaleBiscuitPriceModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        queryset = SaleBiscuitPrice.objects.all()
        serializer = SaleBiscuitPriceDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class SaleBiscuitPriceDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return SaleBiscuitPrice.objects.get(pk=pk)
        except SaleBiscuitPrice.DoesNotExist:
            raise ValidationError('not found')

    def put(self, request, pk):
        data = request.data
        try:
            biscuit = data['biscuit']
        except KeyError:
            raise ValidationError('biscuit not found')
        default_price = get_biscuit_price(biscuit)
        data['default_price'] = default_price
        queryset = self.get_object(pk)
        serializer = SaleBiscuitPriceModelSerializer(queryset,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SaleBiscuitPriceDetailModelSerializer(queryset, many=False)
        return Response(serializer.data)

