from apps.recipe.models.biscuit_recipe import BiscuitRecipe
from api.recipe.serializers.biscuit_recipe import BiscuitRecipeSerializer, BiscuitRecipeDetailSerializer
from apps.biscuit.models.biscuit import Biscuit
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.biscuit.utils.biscuit import get_biscuit, get_biscuit_recipe
from rest_framework.permissions import IsAuthenticated


class RetseptListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        for i in data:
            json_data = i
            serializer = BiscuitRecipeSerializer(data=json_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": 200})

    def get(self, request):
        recipes = BiscuitRecipe.objects.all()
        serializer = BiscuitRecipeDetailSerializer(recipes, many=True)
        return Response(serializer.data)


class RetseptDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        from apps.biscuit.utils.biscuit import get_biscuit
        data = request.data
        biscuit_id = self.request.GET.get('biscuit_id', None)
        get_biscuit = get_biscuit(biscuit_id)
        BiscuitRecipe.objects.filter(biscuit=get_biscuit).delete()
        for i in data:
            serializer = BiscuitRecipeSerializer(data=i)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({'code': 200})

    def get(self, request, *args, **kwargs):
        from apps.biscuit.utils.biscuit import get_biscuit
        biscuit_id = self.request.GET.get('biscuit_id', None)
        get_biscuit = get_biscuit(biscuit_id)
        recipes = get_biscuit_recipe(get_biscuit)
        serializer = BiscuitRecipeDetailSerializer(recipes, many=True)
        return Response(serializer.data)











