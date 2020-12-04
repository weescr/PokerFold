from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile
from game.models import Game

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class GameSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Game
        fields = ('id', 'status')
        
