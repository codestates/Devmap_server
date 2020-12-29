from .serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    ChangePasswordSerializer,
    SignInfoSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Signin Token
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# Signup
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Signinfo
def SignInfoView(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserinfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

# change_password
class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer