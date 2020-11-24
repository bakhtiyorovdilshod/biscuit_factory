from rest_framework.serializers import ModelSerializer
from apps.recipe.models.biscuit_recipe import BiscuitRecipe
from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.product.serializers.product import ProductModelSerializer


class BiscuitRecipeSerializer(ModelSerializer):
    class Meta:
        model = BiscuitRecipe
        fields = [
            'biscuit',
            'product',
            'value',
            'unit_of_measurement'
        ]


class BiscuitRecipeDetailSerializer(ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)
    product = ProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = BiscuitRecipe
        fields = [
            'biscuit',
            'product',
            'value',
            'unit_of_measurement'
        ]







