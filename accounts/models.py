from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # username = models.CharField(max_length=40, unique=False, default='')
    pass
