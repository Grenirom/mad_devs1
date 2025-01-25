from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('doctor', 'Доктор'),
        ('patient', 'Пациент')
    )
    role = models.CharField(max_length=20, choices=ROLES)


class Patient(models.Model):
    date_of_birth = models.DateField()
    diagnoses = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

