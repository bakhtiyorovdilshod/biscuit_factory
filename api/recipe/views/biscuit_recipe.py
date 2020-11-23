from rest_framework.viewsets import ModelViewSet
from apps.recipe.models.biscuit_recipe import BiscuitRecipe
from api.recipe.serializers.biscuit_recipe import BiscuitRecipeSerializer


class BiscuitRecipeModelViewSet(ModelViewSet):
    queryset = BiscuitRecipe.objects.all()
    serializer_class = BiscuitRecipeSerializer











