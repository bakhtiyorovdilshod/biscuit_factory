from rest_framework.serializers import ModelSerializer
from apps.product.models.product import Product, ManufacturedProduct, ManufacturedProductPriceList
from api.supplier.serializers.supplier import SupplierSerializer


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(ProductModelSerializer, self).run_validators(value)

    def create(self, validated_data):
        name = validated_data.pop('name')
        product, _ = Product.objects.get_or_create(name=name, **validated_data)
        return product


class ProductDetailSerializer(ModelSerializer):
    supplier = SupplierSerializer(read_only=True, many=False)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'unit_of_measurement',
            'supplier',
            'created_date',
            'modified_date',
            'description'
        ]


class ManufacturedProductModelSerializer(ModelSerializer):
    class Meta:
        model = ManufacturedProduct
        fields = "__all__"

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(ManufacturedProductModelSerializer, self).run_validators(value)

    def create(self, validated_data):
        name = validated_data.pop('name')
        price = validated_data.pop('price')
        product, _ = ManufacturedProduct.objects.get_or_create(name=name, **validated_data)
        ManufacturedProductPriceList.objects.create(product=product,price=price)
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        obj = ManufacturedProductPriceList.objects.get(id=1)
        obj.price = validated_data.get('price', instance.price)
        obj.save()
        return instance








