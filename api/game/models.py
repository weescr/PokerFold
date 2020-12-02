from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	status = models.IntegerField(default = 0)  #0 - ожидание игроков | 1 - игра в процессе | игра закончена
	players = models.CharField(max_length = 250) # uli nick tim

	def __str__(self):
		return str(self.status)

	def player_info(self,nickname):
		st = list(self.players.split(' '))
		try:
			u_name = st[st.index(nickname)]
		except:
			return "invalid user"
		return User.objects.get(username__exact = u_name)