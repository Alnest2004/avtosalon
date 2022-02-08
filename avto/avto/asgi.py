"""
ASGI config for avto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# ASGI — это интерфейс для коммуникации между приложениями и серверами.
# ASGI — это формат сообщения и то, как эти сообщения должны передаваться
# между приложением и сервером протокола, который его запускает.
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avto.settings')

application = get_asgi_application()
