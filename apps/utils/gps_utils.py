# _*_ coding:utf-8 _*_
"""
gps公共函数
"""
import json
import time
from datetime import datetime

import requests

from apps.gps.consumers import push
from apps.models.gps_md import GpsModel


def get_gps_info_func(gps_str):
    """
    获得gps定位上传的位置信息,对数据进行解析
    """
    # 根据gps终端传来的信息判断是否为位置信息
    # 如果为位置信息，保存数据库
    if 'UD' in gps_str:
        # 解析出对应的经度、纬度和设备编码
        longitude_str = gps_str.split('N,')[1].split(',E,')[0]
        latitude_str = gps_str.split(',N,')[0].split(',')[-1]
        gps_code = gps_str.split(',')[0].split('*')[1]
        # 将gps位置信息保存到数据库中
        gps_data = {'gps_code': gps_code, 'longitude': longitude_str, 'latitude': latitude_str}
        GpsModel.objects.create(**gps_data)
        # 同时将数据推送到前端页面，channles的group_name为“push_gps_info”
        now_time_str = str(datetime.now())
        # 转换成json格式，传给前端供实时显示
        real_time_gps_data = {
            'gps_code': gps_code,
            'longitude': longitude_str,
            'latitude': latitude_str,
            'create_time': now_time_str
        }
        gps_data_str = real_time_gps_data
        push('push_gps_info', gps_data_str)
    else:
        return_info = "It's not position info"


def judge_entry_geofence_func(location_str):
    """
    判断是否进入到电子围栏内
    @location_str: 经纬度信息
    """
    time_str = int(time.time())
    url = 'https://restapi.amap.com/v4/geofence/status'

    payload = {
        'key': '129ed5524f7785b3926273169b086906',
        'diu': 'gp1440392518291',
        'locations': "30.270918,119.963193,%s" % time_str,
    }
    r = requests.get(url, params=payload)
    print(r.text)


