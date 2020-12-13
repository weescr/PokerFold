from django.urls import path
from . impo rt views

app_name = 'api'

urlpatterns = [
	path('',views.index,name='index'), # GET
    path('users/',views.list_users,name='list_users'), # GET
    path('game/list/',views.list_games,name='list_games'), # GET
    #tokens
    path('token/get/', views.get_new_token, name = None), # POST
    path('token/<str:pk>/delete/',views.delete_token,name= None), # GET
    path('token/<str:pk>/status/',views.token_status,name= None), # GET
    #in-game all requests are POST
    path('game/<int:id>/',views.game_info,name= None), # GET
    path('game/create/',views.create_game, name = None),
    path('game/<int:id>/join/',views.join_the_game,name= None),
    path('game/<int:id>/leave/',views.leave_the_game,name= None),
    path('game/<int:id>/logs/',views.view_game_logs,name= None),
    path('game/<int:id>/secret/<str:pk>/',views.get_secret_information_player,name= None),
    path('game/<int:id>/secret/<str:pk>/action/',views.player_game_action,name= None),
]
