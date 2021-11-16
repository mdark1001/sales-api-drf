"""  """
from rest_framework.viewsets import ModelViewSet

from api.models import Team
from api.serializers.teams import TeamModelSerializer


class TeamModelViewSet(ModelViewSet):
    serializer_class = TeamModelSerializer
    queryset = Team.objects.all()
    lookup_field = 'slug_name'
