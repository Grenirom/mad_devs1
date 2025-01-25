from django.contrib import admin
from django.contrib.admin import ModelAdmin

from patients.models import Patient, User

class PatientModelAdmin(ModelAdmin):
    list_display = ['id', 'date_of_birth']


class UserModelAdmin(ModelAdmin):
    list_display = ['id', 'role', 'username']

admin.site.register(User, UserModelAdmin)
admin.site.register(Patient, PatientModelAdmin)
