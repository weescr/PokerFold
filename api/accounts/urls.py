from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('',views.index,name='index'),
	path('<str:username>',views.userpage,name='userpage'),
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
	path('<str:username>/stats',views.stats, name="stats"),
	path('api/users/', views.UserListView.as_view(), name=None),
	path('api/users/create/', views.UserCreateView.as_view(), name=None),
	path('api/users/<int:pk>/', views.UserDetailView.as_view(), name=None)
]
