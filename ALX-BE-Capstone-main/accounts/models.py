from django.contrib.auth.models import AbstractUser
from django.db import models

# Model representing a User
class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
