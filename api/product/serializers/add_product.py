from rest_framework.serializers import ModelSerializer

from api.product.utils.product import add_product_to_warehouse, add_product_to_warehouse_update, \
    manufactured_product_add, manufactured_product_add_update
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

    def validate(self, attrs):
        if not attrs.get('product'):
            raise ValidationError({'error': 'Product not found'})
        if not attrs.get('quantity'):
            raise ValidationError({'error': 'quantity not found'})
        if not attrs.get('currency'):
            raise ValidationError({'error': 'currency not found'})
        if not attrs.get('price'):
            raise ValidationError({'error': 'price not found'})
        if not attrs.get('supplier'):
            raise ValidationError({'error': 'supplier not found'})
        return attrs

    def create(self, validated_data):
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        currency = validated_data.get('currency')
        price = validated_data.get('price')
        supplier = validated_data.get('supplier')
        instance = AddProduct.objects.create(product=product, quantity=quantity,currency=currency,price=price,supplier=supplier)
        add_product_to_warehouse(validated_data)
        return instance

    def update(self, instance, validated_data):
        add_product_to_warehouse_update(instance, validated_data)
        instance.biscuit = validated_data.get('biscuit', instance.biscuit)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.price = validated_data.get('price', instance.price)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.save()
        return instance


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

    def validate(self, attrs):
        from apps.product.utils.product import get_product_recipe
        if not attrs.get('product'):
            raise ValidationError({'error': 'Product not found'})
        if not attrs.get('quantity'):
            raise ValidationError({'error': 'quantity not found'})
        recipes = get_product_recipe(attrs.get('product'))
        if check_warehouse_product_quantity(recipes, attrs.get('quantity'))!=len(recipes):
            raise ValidationError({'xatolik': 'omborda yetarli mahsulot yoq'})
        if len(recipes)==0:
            raise ValidationError({'xatolik': 'Mahsulot retsepti topilmadi'})
        return attrs

    def create(self, validated_data):
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        instance = AddManufacturedProduct.objects.create(product=product, quantity=quantity)
        manufactured_product_add(validated_data)
        return instance

    def update(self, instance, validated_data):
        manufactured_product_add_update(instance, validated_data)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance


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
            raise ValidationError('omborda yetarli mahsulot yoq')