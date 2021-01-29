from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from rest_framework.serializers import ValidationError

from api.order.serializers.order import ClientOrderModelSerializer, ClientOrderDetailModelSerializer
from apps.order.models.order import ClientOrder


class ClientOrderModelViewSet(viewsets.ModelViewSet):
    queryset = ClientOrder.objects.all()
    serializer_class = ClientOrderModelSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        serializer = ClientOrderDetailModelSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, *args, **kwargs):
        queryset = self.get_object()
        serializer = ClientOrderDetailModelSerializer(queryset, many=False)
        return Response(serializer.data)