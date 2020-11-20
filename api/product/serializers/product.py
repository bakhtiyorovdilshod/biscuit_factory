from rest_framework.serializers import ModelSerializer
from apps.product.models.product import Product


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











