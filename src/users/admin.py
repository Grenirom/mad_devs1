from django.contrib import admin
from django.contrib.admin import ModelAdmin

from src.users.models import User


class UserModelAdmin(ModelAdmin):
    list_display = ['id', 'role', 'username']

admin.site.register(User, UserModelAdmin)