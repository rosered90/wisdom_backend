# _*_ coding:utf-8 _*_
import json

import requests

url = 'https://restapi.amap.com/v4/geofence/meta?key=129ed5524f7785b3926273169b086906'


def create_geofence_func():
    """
    创建电子围栏（地理围栏）
    """
    payload = {
        'name': 'AiTown',
        # 创建不同的地理围栏时可修改：创建多边形的经纬度，用;分开每一个点的经纬度
        'points': '119.962233,30.271154;119.965687,30.272016;119.9658,30.26887;119.962549,30.268564',
        "repeat": "Mon,Tues,Wed,Thur,Fri,Sat,Sun",
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.text)
    if 'message' in result['data']:
        print(result['data']['message'])


def show_geofence_func():
    """
    查看电子围栏
    """
    r = requests.get(url)
    print(r.text)



if __name__ == '__main__':
    # 创建电子围栏
    # create_geofence_func()
    # 查看电子围栏
    show_geofence_func()
