"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

class WSGIApplication:
    def __init__(self):
        self.settings_module = 'bookstore.settings'

    def setup_environment(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_module)

    def get_application(self):
        self.setup_environment()
        return get_wsgi_application()

application = WSGIApplication().get_application()
