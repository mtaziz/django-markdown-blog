from django.db import models
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager


class PostManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(status=Post.STATUS_PUBLISHED, published__lte=timezone.now())


class ContentBase(models.Model):
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

    objects = PostManager()

    class Meta:
        abstract = True
        ordering = ['-published', ]

    def is_published(self):
        return self.published <= timezone.now() and self.status == Post.STATUS_PUBLISHED


class Post(ContentBase):

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-published', ]

    def __str__(self):
        return 'Post: {}'.format(self.title or self.slug)

    def get_absolute_url(self):
        return reverse('post', args=[self.published.year, self.id])


class Page(ContentBase):

    show_in_menu = models.BooleanField()

    def __str__(self):
        return 'Page: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('page', args=[self.slug])
