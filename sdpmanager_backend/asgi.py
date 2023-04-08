"""
ASGI config for sdpmanager_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application


django.setup()
django_asgi_app = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing      # 这个文件后续会说，你先写上。

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdpmanager_backend.settings')

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,     # http走Django默认的asgi
        "websocket": URLRouter(routing.websocket_urlpatterns),         # websocket走channels
    }
)

