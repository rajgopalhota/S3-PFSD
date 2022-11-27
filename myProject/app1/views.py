from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

def Hello(request):
    return HttpResponse("Welcome to Django")

def Login(request):
    return render(request, 'login.html')
