from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(response):
    return render(response, "app/hello.html", {})