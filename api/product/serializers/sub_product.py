from rest_framework.serializers import ModelSerializer
from apps.product.models.sub_product import SubProduct


class SubProductModelSerializer(ModelSerializer):
    class Meta:
        model = SubProduct
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.total_price = validated_data.get('total_price', instance.address)
        instance.save()
        return instance
