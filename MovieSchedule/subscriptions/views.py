from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'subscriptions/home.html')

def login(request):
    return render(request, 'subscriptions/login.html', context={'title': 'Login'})

def manage(request):
    current_user = User.objects.first()
    
    return render(request, 'subscriptions/manage.html', context={'title': 'Manage', 'user': current_user, 'subscriptions':current_user.subscription_set.all()})