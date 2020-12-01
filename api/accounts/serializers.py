from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['sex','money','in_game']
