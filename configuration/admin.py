from django.contrib import admin

from .models import BlogConfiguration, SocialLink


admin.site.register(BlogConfiguration)
admin.site.register(SocialLink)
