from django.urls import path
from rest_framework import routers
from .views import SignUpViewSet
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('signup', SignUpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]