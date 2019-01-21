from django.contrib import admin

from .models import Article
from .forms import ArticleAdminForm

class ArticleAdmin(admin.ModelAdmin):
	form = ArticleAdminForm
	search_fields = ('title', )

admin.site.register(Article, ArticleAdmin)
