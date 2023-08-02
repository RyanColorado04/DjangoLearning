from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# extend existing Abstract user
class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)
    quick_description = models.CharField(max_length = 200)

