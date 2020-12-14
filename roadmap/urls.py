import roadmap.views
from django.urls import path

urlpatterns = [
    path('', roadmap.views.index.as_view(), name='index'),
    path('signup/', roadmap.views.signup.as_view(), name="signup"),
    path('signin/', roadmap.views.signin.as_view(), name="signin"),
    path('signout/', roadmap.views.signout.as_view(), name="signout"),
    path('memberinfo/', roadmap.views.meberinfo.as_view(), name="memberinfo"),
]