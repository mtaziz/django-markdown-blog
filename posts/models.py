from django.db import models
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager


class PostManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(status=Post.STATUS_PUBLISHED)


class Post(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLISHED = 2

    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    )

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=500, blank=True, default='')
    slug = models.SlugField()
    featured = models.BooleanField(default=False)

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS_CHOICES)

    tags = TaggableManager(blank=True)

    objects = PostManager()

    class Meta:
        ordering = ['-published', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[self.published.year, self.id])

    def is_published(self):
        return self.published <= timezone.now() and self.status == Post.STATUS_PUBLISHED
