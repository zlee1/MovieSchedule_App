from rest_framework import serializers

from django.contrib.auth.models import User
from subscriptions.models import Theater, Subscription

class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Subscription
        fields = ('user_id', 'theater_id')

class TheaterSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Theater
        fields = ('id', 'url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email', 'is_active')
