from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subscriptions-home')
    ,path('home/', views.home, name='subscriptions-home')
    ,path('login/', views.login, name='subscriptions-login')
    ,path('manage/', views.manage, name='subscriptions-manage')
]