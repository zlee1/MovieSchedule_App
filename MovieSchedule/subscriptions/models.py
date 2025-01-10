from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Theater(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_subscribed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name} - {self.theater.name}'