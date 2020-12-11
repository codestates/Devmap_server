from django.contrib import admin
from .models import User, Roadmap, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Roadmap)
admin.site.register(Comment)