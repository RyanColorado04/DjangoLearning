from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_project import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Doll(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return repr('repr ' + self.title )