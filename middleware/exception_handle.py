# -*- coding: utf-8 -*-

import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('alert')
logger.name = __name__

class ExceptionMiddleware(MiddlewareMixin):
	"""
	Exception midldle ware
	"""

	def process_exception(self, request, exception):
		logger.exception(exception)
		return None
