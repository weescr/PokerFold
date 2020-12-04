from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('',views.index,name='index'),
	path('<str:username>',views.userpage,name='userpage'),
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
	path('<str:username>/stats',views.stats, name="stats"),
]
