from django.db import models

# Create your models here.

class UserRole(models.Model):
    name = models.CharField(max_length=100, unique=True)