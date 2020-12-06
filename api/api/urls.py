from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
	path('',views.index,name='index'),
    path('users/',views.list_users,name='list_users'),
    path('games/',views.list_games,name='list_games'),
    path('games/create/',views.create_game, name = None),
    path('games/<int:pk>',views.game_by_id, name= None)
]
