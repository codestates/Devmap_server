from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.views.generic import TemplateView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'mypage', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('users/', include('user.urls')),
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', TemplateView.as_view(template_name="index.html")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]