from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game
from accounts.models import Profile

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['sex','money','in_game']
