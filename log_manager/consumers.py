import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.forms import model_to_dict

from log_manager import models


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.log_name = self.scope['url_route']['kwargs']['log_name']
        self.log_group_name = 'log_%s' % self.log_name

        # Join room group
        await self.channel_layer.group_add(
            self.log_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        print(code)
        await (self.channel_layer.group_discard)(
            self.log_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        print('in send_chat_message')
        text_data_json = json.loads(text_data)
        message = text_data_json
        await createdata(message)
        print(message)
        await self.send(text_data=json.dumps(
            {
                'message': message
            }))

@database_sync_to_async
def getdata():
    db = models.Logs.objects.all()
    print(db,'asdasdasd')
    return models.queryset_to_list(db)


@database_sync_to_async
def createdata(text_data_json):
    Msg_json = json.loads(text_data_json['Msg'])
    print(Msg_json)
    if 'data' in Msg_json:
        db = models.Logs.objects.create(
            sdpid=text_data_json['from'],
            action=Msg_json['action'],
            upload_date=text_data_json['upload_date'],
            data=Msg_json['data']
        )
    else:
        db = models.Logs.objects.create(
            sdpid=text_data_json['from'],
            action=Msg_json['action'],
            upload_date=text_data_json['upload_date'],
        )

    print(db,'asdasdasd')
    return model_to_dict(db)

