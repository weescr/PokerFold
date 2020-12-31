import uuid
from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User

class Token(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	hash = models.CharField(max_length = 250,default = "")
	avaliable_scopes = (
		('AUTH','authicate'),
		)
	scope = models.IntegerField(default = 0,choices=avaliable_scopes)

	
		
