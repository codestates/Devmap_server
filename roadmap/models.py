from django.db import models
from django.conf import settings

# Create your models here.

class Roadmap(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    commentsid = models.ForeignKey('comment.Comment', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    frontback = models.IntegerField(default=0) 
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'roadmaps'