"""
@author: Miguel Cabrera
"""
from rest_framework import serializers
from api.models import Client


class ClientModelSerializer(serializers.ModelSerializer):
    """ Model Serializer for client model """

    class Meta:
        model = Client
        fields = ('name', 'last_name', 'id',)
