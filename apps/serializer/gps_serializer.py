# _*_ coding:utf-8 _*_
from rest_framework import serializers

from apps.models.gps_md import GpsModel


class GpsModelSerializer(serializers.ModelSerializer):
    """
    gps位置信息
    """

    class Meta:
        model = GpsModel
        fields = '__all__'
