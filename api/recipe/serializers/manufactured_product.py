from rest_framework.serializers import ModelSerializer
from apps.recipe.models.manufactured_product import ManufacturedProductRecipe
from api.product.serializers.product import ManufacturedProductModelSerializer
from api.product.serializers.product import ProductModelSerializer


class ManufacturedProductRecipeSerializer(ModelSerializer):
    class Meta:
        model = ManufacturedProductRecipe
        fields = [
            'manufactured_product',
            'product',
            'value',
            'unit_of_measurement'
        ]


class ManufacturedProductRecipeDetailSerializer(ModelSerializer):
    manufactured_product = ManufacturedProductModelSerializer(read_only=True, many=False)
    product = ProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = ManufacturedProductRecipe
        fields = [
            'id',
            'manufactured_product',
            'product',
            'value',
            'unit_of_measurement'
        ]

