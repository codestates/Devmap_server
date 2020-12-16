from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import SignUpSerializer

# Create your views here.

# SignUp
class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer