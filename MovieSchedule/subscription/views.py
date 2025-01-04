from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def login(request):
    return HttpResponse('<h1>Login</h1>')

def user_settings(request):
    return HttpResponse('<h1>Settings</h1>')