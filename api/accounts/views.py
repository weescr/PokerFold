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
	return HttpResponse('<h1>{}|{}</h1>'.format(user.username,user.profile.money))

def register(request):
	form = RegistrationForm(request.POST or None)
	if request.POST and form.is_valid():
	    username = form.cleaned_data['email']
	    password = form.cleaned_data['password']
	    user = User.objects.create_user(username,username,password)
	    login(request, user)
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

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserCreateView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer

	def create(self, request, *args, **kwargs):
		#super(UserCreateView, self).create(request, args, kwargs)
		u = User.objects.create_user(request.data.get('username'),request.data.get('username'),request.data.get('password'))
		response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": u.username, "pass": u.password}
		return Response(response)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = serializers.ProfileSerializer
	def retrieve(self, request, *args, **kwargs):
		super(UserDetailView, self).retrieve(request, args, kwargs)
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		data = serializer.data
		response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result_for_profile": data}
		return Response(response)

	def patch(self, request, *args, **kwargs):
		super(UsertDetailView, self).patch(request, args, kwargs)
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		data = serializer.data
		response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
		return Response(response)
	def delete(self, request, *args, **kwargs):
		super(UserDetailView, self).delete(request, args, kwargs)
		response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
		return Response(response)
