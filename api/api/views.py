from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
from game.models import Game
from accounts.models import Profile
from . import handler
from django.contrib.auth import authenticate, login
import uuid
from .models import Token

def random__hash():
    return uuid.uuid4().hex

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
    Users = User.objects.all()
    serializer1 = serializers.UserSerializer(Users,many=True)
    serializer = serializers.GameSerializer(queryset, many=True)
    return Response(serializer1.data + serializer.data)

@api_view(['POST'])
def create_game(request):
    try:
        owner = User.objects.get(id=request.data.get('id'))
        game = Game.objects.create(game_owner=owner.id,players=owner.username)
    except:
        return Response("error")
    in_game_players = []
    for player_name in list(game.players.split(" ")):
        player = User.objects.get(username__exact = player_name)
        p = serializers.UserSerializer(player)
        in_game_players.append(p.data)
    jsong_obj = {
        'PokerFold: Game': "version 0.01",
        'id':game.id,
        'status':game.status,
        'owner':game.game_owner,
        'players': in_game_players,
    }
    handler.write_game(game.id,jsong_obj)
    return Response("succes!")

@api_view(['GET'])
def game_by_id(request,pk):
    game = Game.objects.get(id=pk)
    serializer = serializers.GameSerializer(game)
    game_obj = handler.read_game(pk)
    new_players = []
    for player_json in game_obj['players']:
        new_player_obj = User.objects.get(username__exact = player_json['username'])
        serializer2 = serializers.UserSerializer(new_player_obj)
        new_players.append(serializer2.data)
    game_obj['players'] = new_players
    
    return Response(game_obj)

@api_view(['POST'])
def get_token(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print('username:',username,'password:',password)
    user = authenticate(request,username=username, password=password)
    if not user:
        return Response('auth failed')
    #login(request, user)
    token = Token.objects.create(user=user,hash=random__hash(),scope=1)
    obj = {
        'username': user.username,
        'token': token.hash
    }
    return Response(obj)

@api_view(['POST'])
def join_the_game(request):
    pass

