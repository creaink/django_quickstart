# -*- coding: utf-8 -*-
import os
import random
from datetime import datetime

def upload_path(instance, filename):
	"""use for override path generate function for models,
	Usage:
		image = models.ImageField(upload_to=upload_path)
	"""
	ext = os.path.splitext(filename)[1]
	dt = datetime.now()
	name = 'f_' + dt.strftime('%H%M%S') + '_%010x' % random.randrange(16**10) + ext
	return '{0}/{1}/{2}'.format(str.lower(instance.__class__.__name__), dt.strftime('%Y/%m/%d'), name)
