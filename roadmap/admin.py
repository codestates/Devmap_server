from django.contrib import admin
from .models import Users, Roadmaps, Comments

# # Register your models here.

admin.site.register(Users)
admin.site.register(Roadmaps)
admin.site.register(Comments)