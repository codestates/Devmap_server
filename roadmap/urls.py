import roadmap.views
from django.urls import path

urlpatterns = [
    path('signup/', roadmap.views.SignUp, name="signup"),
]