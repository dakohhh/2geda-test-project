from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    username = None

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []
