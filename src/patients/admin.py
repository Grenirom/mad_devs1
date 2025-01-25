from django.contrib import admin
from django.contrib.admin import ModelAdmin

from src.patients.models import Patient

class PatientModelAdmin(ModelAdmin):
    list_display = ['id', 'date_of_birth']

admin.site.register(Patient, PatientModelAdmin)
