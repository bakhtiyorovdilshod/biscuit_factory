from rest_framework import viewsets

from api.product.serializers.add_product import ProductAddListModelSerializer, ProductAddDetailModelSerializer, \
    ProductUpdateModelSerializer
from apps.product.models import Product
from apps.product.models.add_product import AddProduct
from apps.warehouse.models.product import WareHouseProduct
from api.warehouse.serializers.add_product import ProductAddUpdateModelSerializer, ProductFullUpdateModelSerializer
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
        quantity = data['quantity']
        product_id = data['product']
        price = data['price']
        total_price = quantity * price
        serializer = ProductAddListModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        warehouse_product_data = {}
        warehouse_product_data['quantity'] = quantity
        product = self.get_warehouse_product(product_id)
        warehouse_serializer = ProductAddUpdateModelSerializer(product, data=warehouse_product_data)
        warehouse_serializer.is_valid(raise_exception=True)
        warehouse_serializer.save()
        product.total_price += total_price
        product.set_average_price()
        product.save()
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
        price = data['price']
        quantity = data['quantity']
        product = data['product']
        prev_product = self.get_object(pk)
        warehouse_product = self.get_warehouse_product(prev_product.product)
        warehouse_product.quantity-=prev_product.quantity
        if warehouse_product.quantity == 0:
            warehouse_product.total_price = 0
            warehouse_product.average_price = 0
        else:
            prev_total_price = prev_product.price * prev_product.quantity
            warehouse_product.total_price-=prev_total_price
            warehouse_product.set_average_price()
        warehouse_product.save()
        next_product_id = self.get_product(product)
        next_warehouse_product = self.get_warehouse_product(next_product_id)
        next_warehouse_product.quantity+=quantity
        new_total_price = price * quantity
        next_warehouse_product.total_price+=new_total_price
        next_warehouse_product.set_average_price()
        next_warehouse_product.save()
        serializer = ProductUpdateModelSerializer(prev_product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)









