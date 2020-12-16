from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', include('roadmap.urls')),
    path('admin/', admin.site.urls),
    path('users/signin/', obtain_auth_token)
]