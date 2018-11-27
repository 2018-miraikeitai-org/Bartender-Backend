#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
WSGI config for bartender project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import threading
import time
import schedule
from recommend import collaborative_filtering

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bartender.settings')

application = get_wsgi_application()


def awake():
    schedule.every().day.at("1:06").do(collaborative_filtering.collaborative_filtering, )
    while True:
        schedule.run_pending()
        time.sleep(1)


t = threading.Thread(target=awake)
t.start()
