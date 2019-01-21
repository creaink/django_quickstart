import os
import logging

from django.shortcuts import render, HttpResponse
from django.views.generic import FormView
from django.conf import settings
from django.utils.encoding import filepath_to_uri

from .forms import ArticleForm
from django_quickstart.task import add

logger = logging.getLogger(__name__)

class ArticleView(FormView):
	template_name = 'article.html'
	form_class = ArticleForm
	success_url = '/'

	def form_valid(self, form):
		# do something
		return super().form_valid(form)

def handle_uploaded_file(f):
	path = os.path.join(settings.MEDIA_ROOT, f.name)
	with open(path, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	return filepath_to_uri(os.path.join(settings.MEDIA_URL + f.name))

def ImageHandler(request):
	# 简单的示范，推荐使用 ImageFild Model + restframework 完成
	img_url = handle_uploaded_file(request.FILES["img"])
	return HttpResponse('{"img":"%s"}'%(img_url), status=201)

def CeleryHandler(request):
	add.delay(1, 2)
	logger.error("celery")
	return HttpResponse(b"OK !")
