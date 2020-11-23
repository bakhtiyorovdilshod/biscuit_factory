from rest_framework.serializers import ModelSerializer
from apps.supplier.models.supplier import Supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

