# -*- coding: utf-8 -*-
from django.urls import path
from .views import ArticleView, CeleryHandler, ImageHandler

# needed for include and namespace
app_name = 'article'
urlpatterns = [
	path('test/', view=ArticleView.as_view(), name='article'),
	path('img/', ImageHandler, name='img'),
	path('celery/', CeleryHandler, name='celery'),
]
