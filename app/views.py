from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(response):
    return render(response, "app/hello.html", {})

def exp(response):
    return render(response, "app/exp.html", {})   

def proj(response):
    return render(response,"app/proj.html",{} )

def skills(response):
    return render(response, "app/skills.html",{})