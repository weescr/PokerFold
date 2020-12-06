from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate, login
#api
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Profile
# Create your views here.

def index(request):
	return HttpResponse("<h1>Main</h1>")

def userpage(request,username):
	try:
		user = User.objects.get(username__exact = username)
	except:
		return HttpResponse('<h1>Еблан. Такого юзера нет</h1>')
	return render(request,'user.html',{'user':user})

def register(request):
	form = RegistrationForm(request.POST or None)
	if request.POST and form.is_valid():
	    username = form.cleaned_data['email']
	    password = form.cleaned_data['password']
	    user = User.objects.create_user(username,username,password)
	    login(user)
	    return HttpResponse('<h1>Registered</h1>')
	return render(request,'register.html',{'form':form})

def login(request):
	form = LoginForm(request.POST or None)
	if request.POST and form.is_valid():
		username = form.cleaned_data['nick']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		return HttpResponse('<h1>Вы вошли под {}</h1>'.format(user.username))
	return render(request,'login.html',{'form':form})

def stats(request,username):
	try:
		user = User.objects.get(username__exact = username)
	except:
		return HttpResponse('<h1>Господи аа какой ты тупорылый олень! Ты сначала чекни: есть ли такой юзер, а потом мать чекни.</h1>')
	return render(request,'stats.html',{'user':user})
