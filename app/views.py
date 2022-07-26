from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def hello(response):
    return HttpRequest("Wach assat") 