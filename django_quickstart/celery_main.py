from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# FIXME celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_quickstart.settings')

app = Celery('django_quickstart')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# 	such as CELERY_BROKER_URL = 'redis://localhost:6379'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules (name as tasks.py) from all registered Django app configs.
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#	 print('Request: {0!r}'.format(self.request))
