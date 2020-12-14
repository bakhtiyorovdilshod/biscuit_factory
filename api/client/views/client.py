from api.client.serializers.client import ClientModelSerializer
from rest_framework import viewsets
from apps.client.models.client import Client
from rest_framework.permissions import IsAuthenticated


class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
    permission_classes = (IsAuthenticated,)
