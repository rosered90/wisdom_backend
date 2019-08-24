from django.urls import path

from apps.gps.consumers import GpsConsumer

websocket_urlpatterns = [
    path('ws/gps/', GpsConsumer),
]