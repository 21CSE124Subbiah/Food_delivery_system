from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username