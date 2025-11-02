from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


# request -> response
# request handler
# action
# view


def say_hello(request):
    x =1
    y =2
    return HttpResponse('Hello world') 

def say_bye(request):
    return HttpResponse("Bye user!")

def contact(request):
    return render(request, "playground/contact.html")
