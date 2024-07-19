# Jobapp1/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as needed
    
    def __str__(self):
        return self.title

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
