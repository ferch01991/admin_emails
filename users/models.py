from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # Se heredar del modelo user de django
    newsletter = models.BooleanField(default=True)


