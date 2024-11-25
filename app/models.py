from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=255) 
    #FirstName = models.CharField(max_length=255) 
    #LastName = models.CharField(max_length=255) 
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
