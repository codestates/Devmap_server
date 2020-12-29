from .views import RegisterAPI, LoginAPI, memberinfoAPI, ChangePasswordAPI
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('signup/', RegisterAPI.as_view(), name='register'),
    path('signin/', LoginAPI.as_view(), name='login'),
    path('signout/', knox_views.LogoutView.as_view(), name='logout'),
    path('memberinfo/', memberinfoAPI.as_view(), name='memberinfo'),
    path('memberinfochange/<int:pk>/', ChangePasswordAPI.as_view(), name='memberinfochange'),
]