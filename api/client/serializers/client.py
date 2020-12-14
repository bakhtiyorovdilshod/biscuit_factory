from rest_framework.serializers import ModelSerializer
from apps.client.models.client import Client


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
