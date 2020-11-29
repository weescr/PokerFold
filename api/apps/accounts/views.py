from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm

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