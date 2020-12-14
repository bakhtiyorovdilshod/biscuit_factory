from rest_framework import viewsets

from api.product.serializers.add_product import ProductAddListModelSerializer, ProductAddDetailModelSerializer, \
    ProductUpdateModelSerializer, ManufacturedProductAddListModelSerializer, ManufacturedProductUpdateModelSerializer, \
    ManufacturedProductAddDetailModelSerializer
from apps.product.models import Product, ManufacturedProduct
from apps.product.models.add_product import AddProduct, AddManufacturedProduct
from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct
from api.warehouse.serializers.add_product import ProductAddUpdateModelSerializer, ProductFullUpdateModelSerializer, \
    ManufacturedProductAddUpdateModelSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class ProductAddModelViewSet(viewsets.ModelViewSet):
    queryset = AddProduct.objects.all()
    serializer_class = ProductAddListModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return AddProduct.objects.get(pk=pk)
        except AddProduct.DoesNotExist:
            raise Http404

    def get_warehouse_product(self, pk):
        try:
            return WareHouseProduct.objects.get(product=pk)
        except WareHouseProduct.DoesNotExist:
            raise Http404

    def get_product(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404


    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductAddListModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductAddDetailModelSerializer(product, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        added_products = AddProduct.objects.all()
        serializer = ProductAddDetailModelSerializer(added_products, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        data = request.data
        prev_product = self.get_object(pk)
        serializer = ProductUpdateModelSerializer(prev_product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# new one

class ManufacturedProductAddModelViewSet(viewsets.ModelViewSet):
    queryset = AddManufacturedProduct.objects.all()
    serializer_class = ManufacturedProductAddListModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return AddManufacturedProduct.objects.get(pk=pk)
        except AddManufacturedProduct.DoesNotExist:
            raise Http404

    def get_warehouse_product(self, pk):
        try:
            return WareHouseManufacturedProduct.objects.get(manufactured_product=pk)
        except WareHouseManufacturedProduct.DoesNotExist:
            raise Http404

    def get_product(self, pk):
        try:
            return ManufacturedProduct.objects.get(id=pk)
        except ManufacturedProduct.DoesNotExist:
            raise Http404


    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ManufacturedProductAddListModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = ManufacturedProductAddDetailModelSerializer(product, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        added_products = AddManufacturedProduct.objects.all()
        serializer = ManufacturedProductAddDetailModelSerializer(added_products, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        data = request.data
        prev_product = self.get_object(pk)
        serializer = ManufacturedProductUpdateModelSerializer(prev_product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)









