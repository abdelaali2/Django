from django.shortcuts import render
from django.http import HttpResponse as Resp

# Create your views here.


def hello(request):
    return Resp("Hello World!".upper())
