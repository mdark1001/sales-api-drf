"""

"""
from rest_framework import serializers

from api.models import Sales
from api.serializers import ClientModelSerializer, UserSerializer


class SaleModelSerializer(serializers.ModelSerializer):
    client = ClientModelSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Sales
        fields = ('client', 'user', 'amount', 'date',)


class SaleSerializer(serializers.Serializer):
    """ Custom serializer for sales and views  """
    client = ClientModelSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    amount = serializers.FloatField()
    date = serializers.DateField()
