from rest_framework import viewsets
from apps.product.models.product import Product
from api.product.serializers.product import ProductModelSerializer
from rest_framework.permissions import IsAuthenticated
from api.warehouse.serializers.product import WareHouseProductCreateModelSerializer
from rest_framework.response import Response
from django.http import Http404

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
        product_id = serializer.data['id']
        product_data = {}
        product_data['product'] = product_id
        warehouse_product = WareHouseProductCreateModelSerializer(data=product_data)
        warehouse_product.is_valid(raise_exception=True)
        warehouse_product.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ProductModelSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductModelSerializer(product, many=False)
        return Response(serializer.data)




