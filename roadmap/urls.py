import roadmap.views
from django.urls import path

urlpatterns = [
    path('', roadmap.views.index.as_view(), name='index'),
    path('signup/', roadmap.views.SignUp.as_view(), name="signup"),
    path('signin/', roadmap.views.SignIn.as_view(), name="signin"),
    path('signout/', roadmap.views.SignOut.as_view(), name="signout"),
    path('memberinfo/', roadmap.views.MeberInfo.as_view(), name="memberinfo"),
]