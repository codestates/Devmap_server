from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('roadmap.urls')),
    path('users/', include('roadmap.urls')),
    path('admin/', admin.site.urls),
]