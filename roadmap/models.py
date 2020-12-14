from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'

class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    frontback = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    commentsid = models.ForeignKey('Comment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'roadmaps'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    roadmapid = models.ForeignKey('Roadmap', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'