"""
@author: Miguel Cabrera
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name',)
    # profile =
