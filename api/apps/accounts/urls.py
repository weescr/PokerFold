from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('',views.index,name='index'),
	path('<str:username>',views.userpage,name='userpage'),
	path('register/',views.register,name='register'),
	#path('account/complete',views.complete_registration, name='complete_registration')
]
