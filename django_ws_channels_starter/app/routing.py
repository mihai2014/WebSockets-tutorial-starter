# app/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer1.as_asgi()),     # sync
    re_path(r'ws/echo/$', consumers.EchoConsumer.as_asgi()),     # async
    re_path(r'ws/time/$', consumers.TimeConsumer.as_asgi()),     # async
]

