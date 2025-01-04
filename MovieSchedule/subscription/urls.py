from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subscription-home')
    ,path('login/', views.login, name='subscription-login')
    ,path('profile/', views.profile, name='subscription-profile')
]