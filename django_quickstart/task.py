from __future__ import absolute_import, unicode_literals

import os
import time

from celery import shared_task
from celery.task import periodic_task
from celery.task.schedules import crontab

from django.conf import settings

@periodic_task(run_every=crontab(minute=0))
def backup_log():
	"""celery beat scan periodic task, and need a celery worker to execute"""
	print("Tic Toc")

@shared_task
def add(x, y):
	"""for test"""
	return x + y
