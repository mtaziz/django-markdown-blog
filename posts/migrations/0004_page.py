# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 01:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20170710_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('slug', models.SlugField()),
                ('featured', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')])),
                ('show_in_menu', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
                'abstract': False,
            },
        ),
    ]
