from django.db import models
from django.conf import settings

# Create your models here.

class Comment(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    roadmapid = models.ForeignKey('roadmap.Roadmap', on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'comments'