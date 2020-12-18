from .views import RegisterAPI, LoginAPI, ChangePasswordAPI
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('signup/', RegisterAPI.as_view(), name='register'),
    path('signin/', LoginAPI.as_view(), name='login'),
    path('signout/', knox_views.LogoutView.as_view(), name='logout'),
    path('change_password/<int:pk>/', ChangePasswordAPI.as_view(), name='auth_change_password'),
]