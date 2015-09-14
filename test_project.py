#!/usr/bin/env python
from __future__ import unicode_literals

import django
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect


# Configuration
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        MIDDLEWARE_CLASSES=[
        ],
        INSTALLED_APPS=[
        ],
    )
    # Django >=1.7 compatibility
    if hasattr(django, 'setup'):
        django.setup()


# URL Router
urlpatterns = []


# CLI
def main():
    from django.core.management import execute_from_command_line
    execute_from_command_line()


if __name__ == '__main__':
    main()
