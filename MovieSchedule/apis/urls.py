from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import UserViewSet, TheaterViewSet, SubscriptionViewSet

router = routers.DefaultRouter()

router.register('subscriptions', SubscriptionViewSet, basename='api-subscriptions')
router.register('theaters', TheaterViewSet, basename='api-theaters')
router.register('users', UserViewSet, basename='api-users')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', views.obtain_auth_token, name='api-auth')
]