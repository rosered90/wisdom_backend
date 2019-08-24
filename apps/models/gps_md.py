from django.db import models


class GpsModel(models.Model):
    """gps接收信息表"""
    gps_code = models.CharField(max_length=30, verbose_name="gps编号")
    longitude = models.CharField(max_length=100, null=True, blank=True, verbose_name="经度")
    latitude = models.CharField(max_length=100, null=True, blank=True, verbose_name="纬度")
    create_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True, help_text='创建时间')

