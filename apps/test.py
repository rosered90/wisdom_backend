import json
import os

from apps.gps.consumers import push
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wisdom_backend.settings")

now_time_str =str(datetime.datetime.now())
real_time_gps_data = {
            'gps_code': '3500011958',
            'longitude': '119.957195',
            'latitude': '30.273583',
            'create_time': now_time_str
        }
push('push_gps_info', real_time_gps_data)
# push('push_gps_info','设备编码:3500011958, 经度:119.957195, 纬度:30.273583,时间:2019-08-26 02:44:30.649563,')