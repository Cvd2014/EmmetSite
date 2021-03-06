from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    dateCreated = models.DateTimeField(default=timezone.now)
    datePublished = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)

    def publish(self):
        self.datePublished = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    description = models.TextField()
    datePublished = models.DateTimeField(blank=True, null=True)
    publication = models.CharField(max_length=200, default='abc')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    caption = models.CharField(max_length=200)
    catagory = models.CharField(max_length=200)
    platform = models.CharField(max_length=200,default='youtube')

    def __str__(self):
        return self.title
