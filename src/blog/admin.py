from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date', 'author']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
