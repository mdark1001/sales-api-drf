"""
@author: Miguel Cabrera
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers.clients import ClientModelSerializer

from api.models import Client


class ClientViewSet(viewsets.ModelViewSet, viewsets.ViewSet):
    """ """
    serializer_class = ClientModelSerializer
    queryset = Client.objects.all()
    #permission_classes = [IsAuthenticatedOrReadOnly]
