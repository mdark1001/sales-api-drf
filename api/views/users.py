"""

"""
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from api.serializers.users import UserSerializer

Users = get_user_model()


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
