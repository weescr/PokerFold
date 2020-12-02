from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
	path('game/<int:pk>/', views.GameInfoView.as_view(), name=None)
]