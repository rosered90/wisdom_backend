# -*- coding: utf-8 -*-
from django.urls import path

from apps.serializer_views import gps_serializer_views

urlpatterns = [
    path(r"gps/api/v1/", gps_serializer_views.GpsModelView.as_view(), name='gps_list'),
]
