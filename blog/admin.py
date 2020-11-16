from django.contrib import admin
from .models import Post,Comment


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post)
admin.site.register(Comment)
