# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 05:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170709_2225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published']},
        ),
    ]
