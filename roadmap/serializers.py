from rest_framework import serializers
from roadmap.models import Users

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
