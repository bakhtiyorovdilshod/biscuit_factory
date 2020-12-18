from apps.product.utils.product import get_manufactured_product, get_product_recipe
from apps.recipe.models.manufactured_product import ManufacturedProductRecipe
from api.recipe.serializers.manufactured_product import ManufacturedProductRecipeSerializer, ManufacturedProductRecipeDetailSerializer
from apps.product.models.product import ManufacturedProduct
from rest_framework.response import Response
from rest_framework.views import APIView


class ManufacturedProductRetseptListAPIView(APIView):
    def post(self, request):
        data = request.data
        for i in data:
            json_data = i
            serializer = ManufacturedProductRecipeSerializer(data=json_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": 200})

    def get(self, request):
        recipes = ManufacturedProductRecipe.objects.all()
        serializer = ManufacturedProductRecipeDetailSerializer(recipes, many=True)
        return Response(serializer.data)


class ManufacturedProductRetseptDetailAPIView(APIView):
    def put(self, request, *args, **kwargs):
        data = request.data
        product_id = self.request.GET.get('product_id', None)
        get_product = get_manufactured_product(product_id)
        ManufacturedProductRecipe.objects.filter(manufactured_product=get_product).delete()
        for i in data:
            serializer = ManufacturedProductRecipeSerializer(data=i)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({'code': 200})

    def get(self, request, *args, **kwargs):
        product_id = self.request.GET.get('product_id', None)
        get_product = get_manufactured_product(id=product_id)
        recipes = get_product_recipe(get_product)
        serializer = ManufacturedProductRecipeDetailSerializer(recipes, many=True)
        return Response(serializer.data)