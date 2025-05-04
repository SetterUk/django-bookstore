"""
ASGI config for bookstore project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

class ASGIApplication:
    def __init__(self):
        self.settings_module = 'bookstore.settings'

    def setup_environment(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_module)

    def get_application(self):
        self.setup_environment()
        return get_asgi_application()

application = ASGIApplication().get_application()
