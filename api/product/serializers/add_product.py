from rest_framework.serializers import ModelSerializer
from apps.product.models.add_product import AddProduct
from api.product.serializers.product import ProductModelSerializer


class ProductAddListModelSerializer(ModelSerializer):
    class Meta:
        model = AddProduct
        fields = [
            'product',
            'quantity',
            'currency',
            'price'
        ]


class ProductAddDetailModelSerializer(ModelSerializer):
    product = ProductModelSerializer(read_only=True, many=False)
    class Meta:
        model = AddProduct
        fields = [
            'id',
            'product',
            'quantity',
            'currency',
            'price',
            'total_price',
            'supplier',
            'warehouseman',
            'created_date'
        ]


class ProductUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = AddProduct
        fields = [
            'product',
            'quantity',
            'price'
        ]
