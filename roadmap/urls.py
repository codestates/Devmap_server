from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('signup/', RegisterAPI.as_view(), name='register'),
    path('signin/', LoginAPI.as_view(), name='login'),
    path('signout/', knox_views.LogoutView.as_view(), name='logout'),
    path('signoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]