# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publication',
            field=models.CharField(default='abc', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]