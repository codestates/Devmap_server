from django.urls import path
from user.views import (
    MyObtainTokenPairView,
    RegisterView, 
    MemberInfoAPI,
    ChangePasswordView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signin/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('signin/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', RegisterView.as_view(), name='auth_register'),
    path('memberinfo/', MemberInfoAPI, name='memberinfo'),
    path('memberinfochange/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]