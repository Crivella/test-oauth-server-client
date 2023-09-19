from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Downloads(models.Model):
    """Record of downloads"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)