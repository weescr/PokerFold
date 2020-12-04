from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
from game.models import Game
from accounts.models import Profile

@api_view(['GET'])
def index(request):
    return Response("eto api mf")

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_games(request):
    queryset = Game.objects.all()
    #games = Game.objects.all()
    serializer = serializers.GameSerializer(queryset, many=True)
    return Response(serializer.data)

