# _*_ coding:utf-8 _*_
"""
gps公共函数
"""
from datetime import datetime

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
        now_time_str = datetime.now()
        push('push_gps_info', '设备编码:%s, 经度:%s, 纬度:%s,时间:%s, ' % (gps_code, longitude_str, latitude_str, now_time_str))
    else:
        return_info = "It's not position info"