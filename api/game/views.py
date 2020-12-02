from django.shortcuts import render

from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Game
from accounts.serializers import ProfileSerializer
from accounts.models import Profile

class GameView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer

class GameInfoView(generics.ListAPIView):
	queryset = {'game':Game.objects.all()}
	serializer_class = serializers.GameSerializer
