import roadmap.views
from django.urls import path

urlpatterns = [
    path('signup/', roadmap.views.SignUp, name="signup"),
    path('signin/', roadmap.views.SignIn, name="signin"),
    # path('signout/', roadmap.views.SignOut, name="signout"),
]