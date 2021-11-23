from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Room, Message
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm

def registerUser(request):
    form = CreateUserForm()
    if request.method =="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'main/register.html',{'form':form})

def loginPage(request):
    context={}
    return render(request, 'main/login.html', context)

def index(response,roomid):
    room=Room.objects.get(id=roomid)
    return render(response, "main/base.html", {'name':room.name, 'date':room.date, 'description':room.description})

def home(response):
    return render(response, "main/home.html", {})

