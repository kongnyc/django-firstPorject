from django.http import HttpResponse
from django.shortcuts import render


# def homepage(request):
    # return render(request,'homepage.html')
    # return HttpResponse("Home Page")
def index(request):
    return render(request,'homepage.html')
    
    # return HttpResponse("Hello, world. You're at the polls index.",)