from django.contrib.auth.models import User
from django.test import TestCase

from .factories import PostFactory, UserFactory
from .models import Post


class UserFactoryTestCase(TestCase):

    def test_can_create_user(self):
        u = UserFactory()
        self.assertTrue(u.is_active)
        self.assertEqual(User.objects.filter(username=u.username).count(), 1)


class PostFactoryTestCase(TestCase):

    def test_can_create_post(self):
        p = PostFactory()
        self.assertTrue(p.is_published())
        self.assertEqual(Post.objects.count(), 1)

    def test_create_draft_post(self):
        p = PostFactory(status=Post.STATUS_DRAFT)
        self.assertFalse(p.is_published())
        self.assertEqual(Post.objects.count(), 1)


class TaggingTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_tag_filter(self):
        posts_with_no_tag = [PostFactory() for _ in range(10)]
        posts_with_django_tag = [PostFactory() for _ in range(5)]

        for post in posts_with_django_tag:
            post.tags.add('django')

        response = self.client.get('/tag/django/')
        for post in posts_with_django_tag:
            self.assertTrue(post in response.context['object_list'])

        for post in posts_with_no_tag:
            self.assertFalse(post in response.context['object_list'])
