from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, TheaterSerializer, SubscriptionSerializer
from django.contrib.auth.models import User
from subscriptions.models import Theater, Subscription

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()

    serializer_class = SubscriptionSerializer

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theater.objects.all()

    serializer_class = TheaterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer