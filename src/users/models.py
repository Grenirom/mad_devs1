from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('doctor', 'Доктор'),
        ('user', 'Пользователь')
    )
    role = models.CharField(max_length=20, choices=ROLES)

    def save(self, *args, **kwargs):    # using save method to hash password when adding a user via the admin panel
        if not self.pk and not self.password.startswith('pbkdf2_'): # checking if the user is new, and password is not hashed already
            self.set_password(self.password)
        super().save(*args, **kwargs)