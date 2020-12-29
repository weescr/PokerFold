from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
	sex = models.BooleanField('sex',default=False) #False - Девушка. True - Парень
	money = models.IntegerField('all money',default=0)
	in_game = models.BooleanField('in_game',default=False)

	def __str__(self):
		return str(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()