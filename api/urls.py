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
router.register(r'api/sale/user/(?P<user_id>.+)', SalesUserView, basename='sales-user')
router.register(r'api/sale/team/(?P<team_id>.+)', SalesTeamView, basename='sales-team')

urlpatterns = [
    path('', include((router.urls, 'clients'), namespace='api')),
]
