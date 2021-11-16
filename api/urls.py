"""
url.py
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, SalesUserView
from api.views import TeamModelViewSet, SalesModelViewSet, SalesTeamView
from api.views.client import ClientViewSet

router = DefaultRouter()
router.register(r'api/clients', ClientViewSet, basename='clients')
router.register(r'api/users', UserModelViewSet, basename='users')
router.register(r'api/teams', TeamModelViewSet, basename='teams')
router.register(r'api/sales', SalesModelViewSet, basename='sales')
router.register(r'api/sale/(?P<user_id>.+)/user', SalesUserView, basename='sales-user')
# router.register(r'api/sales/team/<slug_name>', SalesTeamView, basename='sales')

urlpatterns = [
    path('', include((router.urls, 'clients'), namespace='api')),
]
