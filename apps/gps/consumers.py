# _*_ coding:utf-8 _*_
"""
gps消息推送的consumers功能
"""
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import channels.layers
from asgiref.sync import async_to_sync


class GpsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'push_gps_info'

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'gps_message',
                'message': message
            }
        )

    async def gps_message(self, event):
        message = '定位信息：' + event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))


# 提供消息推送函数，推送的消息可以通过push函数调用
def push(username, event):
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        username,
        {
            "type": "gps.message",
            "message": event
        }
    )
