import factory

from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    is_active = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    title = factory.Faker('sentence')
    content = factory.Faker('paragraph')

    created = factory.Faker('past_datetime', tzinfo=timezone.get_current_timezone())
    published = factory.Faker('past_datetime', tzinfo=timezone.get_current_timezone())
    status = Post.STATUS_PUBLISHED
