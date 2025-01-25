from django.contrib.postgres.fields import ArrayField
from django.db import models


class Patient(models.Model):
    date_of_birth = models.DateField()
    diagnoses = ArrayField(models.CharField(max_length=255),default=list)
    created_at = models.DateTimeField(auto_now_add=True)

