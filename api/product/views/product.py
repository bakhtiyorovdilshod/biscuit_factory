from rest_framework import viewsets
from apps.product.models.product import Product, ManufacturedProduct
from api.product.serializers.product import ProductModelSerializer, ManufacturedProductModelSerializer, \
    ProductDetailSerializer
from rest_framework.permissions import IsAuthenticated
from api.warehouse.serializers.product import WareHouseProductCreateModelSerializer, \
    WareHouseManufacturedProductCreateModelSerializer
from rest_framework.response import Response
from django.http import Http404

from apps.supplier.models import Supplier
from apps.warehouse.models import WareHouseProduct


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def create(self, request, *args, **kargs):
        data = request.data
        serializer = ProductModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ProductModelSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product, many=False)
        return Response(serializer.data)

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)


class ManufacturedProductModelViewSet(viewsets.ModelViewSet):
    queryset = ManufacturedProduct.objects.all()
    serializer_class = ManufacturedProductModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return ManufacturedProduct.objects.get(pk=pk)
        except ManufacturedProduct.DoesNotExist:
            raise Http404

    def create(self, request, *args, **kargs):
        data = request.data
        serializer = ManufacturedProductModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ManufacturedProductModelSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = ManufacturedProductModelSerializer(product, many=False)
        return Response(serializer.data)




