from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Room, Message
# from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registerUser(request):
    form = CreateUserForm()
    if request.method =="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'main/register.html',{'form':form})

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		return render(request, 'main/login.html', {})

def logoutUser(request):
	logout(request)
	return redirect('home')

def index(response,roomid):
    
    room=Room.objects.get(id=roomid)
    return render(response, "main/base.html", {'name':room.name, 'date':room.date, 'description':room.description})

def home(response):
    return render(response, "main/home.html", {})

