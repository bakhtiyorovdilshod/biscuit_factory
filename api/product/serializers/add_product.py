from rest_framework.serializers import ModelSerializer

from api.supplier.serializers.supplier import SupplierSerializer
from apps.biscuit.utils.biscuit import check_warehouse_product_quantity
from apps.product.models import ManufacturedProduct
from apps.product.models.add_product import AddProduct, AddManufacturedProduct
from api.product.serializers.product import ProductModelSerializer, ManufacturedProductModelSerializer, \
    ProductDetailSerializer
from rest_framework.serializers import ValidationError


class ProductAddListModelSerializer(ModelSerializer):
    class Meta:
        model = AddProduct
        fields = [
            'product',
            'quantity',
            'currency',
            'price',
            'supplier'
        ]


class ProductAddDetailModelSerializer(ModelSerializer):
    product = ProductDetailSerializer(read_only=True, many=False)
    supplier = SupplierSerializer(read_only=True, many=False)
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


class ManufacturedProductAddListModelSerializer(ModelSerializer):
    class Meta:
        model = AddManufacturedProduct
        fields = [
            'product',
            'quantity'
        ]

    def create(self, validated_data):
        from apps.product.utils.product import get_product_recipe
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        recipes = get_product_recipe(product)
        if check_warehouse_product_quantity(recipes, quantity) == len(recipes):
            instance = AddManufacturedProduct.objects.create(product=product, quantity=quantity)
            return instance
        else:
            raise ValidationError('not enough products in warehouse')



class ManufacturedProductAddDetailModelSerializer(ModelSerializer):
    product = ManufacturedProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = AddManufacturedProduct
        fields = [
            'id',
            'product',
            'quantity',
            'warehouseman',
            'created_date'
        ]


class ManufacturedProductUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = AddManufacturedProduct
        fields = [
            'product',
            'quantity',
        ]

    def update(self, instance, validated_data):
        from apps.product.utils.product import get_product_recipe
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        recipes = get_product_recipe(product)
        if check_warehouse_product_quantity(recipes, quantity) == len(recipes):
            instance.product = validated_data.get('product', instance.product)
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.save()
            return instance
        else:
            raise ValidationError('not enough products in warehouse')