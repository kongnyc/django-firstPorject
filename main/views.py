from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Room, Message

# Create your views here.
# def index(response):
#     return HttpResponse("welcome to chat box")

def index(response,roomid):
    room=Room.objects.get(id=roomid)
    # breakpoint()
    return render(response, "main/base.html", {'name':room.name, 'date':print(room.date), 'description':room.description})

def home(response):
    return render(response, "main/home.html", {})
