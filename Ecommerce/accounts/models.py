from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoUser


# Create your models here.

class User(DjangoUser):
    image = models.ImageField(upload_to="accounts/%Y/%m/%d/%h/%M/")