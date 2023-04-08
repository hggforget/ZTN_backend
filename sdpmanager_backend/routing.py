from django.urls import re_path

from log_manager import consumers

websocket_urlpatterns=[
    #使用同步方式实现
    #path('ws/chat/<room_name>/',ChatConsumer),
    #如果使用异步方式实现，路由的视图必须调用as_asgi()
    re_path(r'ws/log_manager/(?P<log_name>\w+)/$', consumers.NotificationConsumer.as_asgi()),
]