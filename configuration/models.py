from django.db import models
from solo.models import SingletonModel


class SocialLink(models.Model):
    url = models.URLField()
    site = models.CharField(max_length=30)

    def __str__(self):
        return self.site

    def icon(self):
        return '/static/supertinysocialicons/{}.svg'.format(self.site)


class BlogConfiguration(SingletonModel):
    title = models.CharField(max_length=200)
    colour = models.CharField(max_length=6, default='495057')
    by_line = models.TextField(blank=True, default='')
    social_links = models.ManyToManyField('SocialLink', blank=True)
    google_analytics = models.CharField(max_length=20, blank=True, default='', help_text="Full Google Analytics code")

    def __str__(self):
        return self.title
