from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=64, unique=True)
    description = models.TextField()
    password= models.CharField(max_length=31,blank=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=DO_NOTHING)
    username= models.CharField(max_length=20)
    time=models.DateField(auto_now_add=True)
    room=models.ForeignKey(Room, on_delete=CASCADE)
    text=models.CharField(max_length=500)
    
    def __str__(self):
        return self.username