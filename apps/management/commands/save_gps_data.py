# coding:utf-8
import datetime
import logging
import socket
import traceback

from django.core.management.base import BaseCommand

from apps.utils.gps_utils import get_gps_info_func

logger = logging.getLogger("django")


class Command(BaseCommand):
    help = '保存gps位置信息到数据库'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--platform_name', type=str)

    def handle(self, *args, **options):
        try:
            sk = socket.socket()  # 创建socket对象
            print(sk)  # 输出socket对象参数
            HOST = '172.27.0.14'  # 指定ip
            PORT = 8000  # 侦听端口
            BUFSIZ = 1024  # 缓存大小
            ADDR = (HOST, PORT)  # 套接字

            sk.bind(ADDR)  # 套接字ip端口进行绑定
            sk.listen(5)  # 等待客户端连接，连接等待数，默认5
            print("waiting...")

            while True:  # 服务器无限循环，conn就是客户端连接过来而在服务端为期生产的一个链接实例
                conn, addr = sk.accept()  # 建立客户端连接，并返回新的套接字和IP地址
                print("Got connection from", addr)
                while True:  # 通讯无限循环
                    data = conn.recv(BUFSIZ)  # 接受数据
                    if not data:
                        break  # 直接回车退出本次连接
                    now_str = datetime.datetime.now()
                    print(now_str)
                    data_str = data.decode()
                    print(data_str)  # 打印接收到的数据
                    # 保存接收位置信息数据到数据库中
                    get_gps_info_func(data_str)
                    # 如果是链路保持发送信号，则服务端需要回复对应的指令给gps终端
                    if 'LK' in data_str:
                        inp = '[3G*3500011958*0002*LK]'
                        conn.send(bytes(inp, 'utf-8'))
                        print(inp + 'send success!!!')
            conn.close()  # 关闭连接
            s.close()  # 关闭连接
        except Exception as e:
            exstr = traceback.format_exc()
            logger.error("save_gps_data_error:%s" % exstr)
