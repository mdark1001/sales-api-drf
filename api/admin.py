from django.contrib import admin
from .models import Team, Sales, Profile, Client


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'team',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name',)


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('client', 'user', 'amount', 'date',)
