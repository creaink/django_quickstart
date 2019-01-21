from django.db import models

# Create your models here.
class Article(models.Model):
	'''article for test
	'''
	title = models.CharField(max_length=30, verbose_name=u'标题')
	content = models.TextField(verbose_name=u'正文')

	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural = verbose_name = u'文章'
