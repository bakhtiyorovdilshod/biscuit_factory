from api.supplier.serializers.supplier import SupplierSerializer
from rest_framework.viewsets import ModelViewSet

from apps.supplier.models import Supplier
from rest_framework.permissions import IsAuthenticated


class SupplierModelViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated,)