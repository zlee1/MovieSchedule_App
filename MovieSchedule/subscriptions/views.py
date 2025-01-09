from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'subscriptions/home.html')

def login(request):
    return render(request, 'subscriptions/login.html')

def profile(request):
    current_user = User.objects.first()
    context = {'user': current_user, 'subscriptions':current_user.subscription_set.all()}
    
    return render(request, 'subscriptions/profile.html', context=context)