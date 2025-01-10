from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subscriptions-home')
    ,path('home/', views.home, name='subscriptions-home')
    ,path('manage/', views.manage, name='subscriptions-manage')
    ,path('search/<str:zip_code>', views.theater_search, name='subscriptions-search')
]