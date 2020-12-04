from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    status = models.IntegerField(default=0)