# -*- coding: utf-8 -*-
from django import forms
from extra_apps.django_tinymce_widget import TinyMCE_Widget

class ArticleForm(forms.Form):
	titile = forms.CharField(max_length=100)
	content = forms.CharField(widget=TinyMCE_Widget(width=1010,
													img_upload_url='/article/img/',
													img_field='img')
							)

class ArticleAdminForm(forms.ModelForm):
	class Meta:
		fields = '__all__'
		widgets = {
			'content': TinyMCE_Widget(width=1010,
									img_upload_url='/article/img/',
									img_field='img')
		}
