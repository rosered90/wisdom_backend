# -*- coding: utf-8 -*-
from django.urls import path

from apps.views import gps_views
from apps.serializer_views import gps_serializer_views

urlpatterns = [
    path(r"gps/api/v1/", gps_serializer_views.GpsModelView.as_view(), name='gps_list'),
    path(r"gps/receive_gps", gps_views.receive_gps, name="receive_gps")
]
