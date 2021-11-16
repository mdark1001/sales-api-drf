""" """
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from api.models import Sales
from api.serializers import SaleModelSerializer, SaleSerializer

User = get_user_model()


class SalesModelViewSet(viewsets.ModelViewSet):
    serializer_class = SaleModelSerializer
    queryset = Sales.objects.all()


class SalesTeamView(GenericAPIView, ListModelMixin):

    def list(self, request, *args, **kwargs):
        pass


class SalesUserView(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    """ Serializer for  specific list of sales per user
        Here we must use GenericViewSet and Mixins by get default routes included on router default
    """
    serializer_class = SaleSerializer

    def dispatch(self, request, *args, **kwargs):
        """Check if user exists """
        get_object_or_404(User, pk=kwargs['user_id'])
        return super(SalesUserView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Filer by user pk
        :return:
        """
        # print(self.kwargs)
        user_pk = self.kwargs.get('user_id')
        return Sales.objects.filter(user__id=user_pk)
