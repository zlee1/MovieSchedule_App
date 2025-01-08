from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

test_profile = {'name': 'Zack', 'zip_codes': [{'zip': '06468', 'active': 1}, {'zip': '10001', 'active': 0}]}

def home(request):
    return render(request, 'subscriptions/home.html')

def login(request):
    return render(request, 'subscriptions/login.html')

def profile(request):
    current_user = User.objects.first()
    context = {'user': current_user, 'subscriptions':current_user.subscription_set.all()}
    
    return render(request, 'subscriptions/profile.html', context=context)