from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import Http404

from api.biscuit.serializers.produce import ProduceBiscuitSerializer, ProduceBiscuitCreateSerializer
from apps.biscuit.models import ProduceBiscuit, Biscuit
from apps.product.models import Product
from apps.recipe.models import BiscuitRecipe
from apps.warehouse.models import WareHouseBiscuit, WareHouseProduct
from rest_framework.response import Response


class ProduceBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = ProduceBiscuit.objects.all()
    serializer_class = ProduceBiscuitSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        biscuit = self.kwargs['pk']
        quantity = data['quantity']
        data['biscuit'] = biscuit
        biscuit = Biscuit.objects.get(id=biscuit)
        ware_biscuit = WareHouseBiscuit.objects.get(biscuit=biscuit)
        recipe = BiscuitRecipe.objects.filter(biscuit=biscuit)
        for i in recipe:
            product = i.product
            value = i.value
            warehouse = WareHouseProduct.objects.get(product=product)
            price = Product.objects.get(id=product.id).price
            quantity_value = quantity*value
            warehouse.quantity -= quantity_value
            new_total_price = price * quantity_value
            warehouse.total_price -= new_total_price
            warehouse.save()
        ware_biscuit.add_quantity(quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.save()
        serializer = ProduceBiscuitCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        produce_id =serializer.data['id']
        obj = ProduceBiscuit.objects.get(id=produce_id)
        obj.set_total_price()
        obj.save()
        serializer = ProduceBiscuitCreateSerializer(obj)
        return Response(serializer.data)