# import django.http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello!")
    #request the html file
    return render(request, "hello/index.html")

def Atiwit(request):
    return HttpResponse("Hello, Atiwit!")

def Cal(request):
    return HttpResponse("You are the calculator!")

def greet(request, name):
    # capitalize function is function taht give the first lettet of the name value for big alphabet
    # return HttpResponse(f"Hello, {name.capitalize()}!")

    # Third argument is called the context and the context is all of the information that I would like to provide to the template
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })