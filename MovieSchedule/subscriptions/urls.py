from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subscriptions-home')
    ,path('about/', views.about, name='subscriptions-about')
    ,path('manage/', views.manage, name='subscriptions-manage')
    ,path('search/<str:zip_code>', views.theater_search, name='subscriptions-search')
    ,path('unsubscribe/<str:theater_id>', views.unsubscribe, name='subscriptions-unsubscribe')
]