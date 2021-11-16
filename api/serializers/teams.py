"""
@author: Miguel Cabrera
"""
from rest_framework import serializers
from api.models import Team


class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'slug_name',)
