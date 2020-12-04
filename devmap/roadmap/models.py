from os import stat
from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

class roadmap(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    frontback = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    userid = models.ForeignKey('users', on_delete=models.CASCADE)
    commentsid = models.ForeignKey('comments', on_delete=models.CASCADE)

class comments(models.Model):
    content = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    userid = models.ForeignKey('users', on_delete=models.CASCADE)
    roadmapid = models.ForeignKey('roadmap', on_delete=models.CASCADE)