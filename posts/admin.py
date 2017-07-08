from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    list_display = ['title', 'slug', 'published']


admin.site.register(Post, PostAdmin)
