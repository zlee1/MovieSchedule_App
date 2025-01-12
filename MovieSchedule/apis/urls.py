from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, TheaterViewSet, SubscriptionViewSet

router = routers.DefaultRouter()

router.register('subscriptions', SubscriptionViewSet)
router.register('theaters', TheaterViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]