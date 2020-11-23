from rest_framework.serializers import ModelSerializer
from apps.recipe.models.biscuit_recipe import BiscuitRecipe


class BiscuitRecipeSerializer(ModelSerializer):
    class Meta:
        model = BiscuitRecipe
        fields = [
            'biscuit',
            'product',
            'value',
            'unit_of_measurement'
        ]







