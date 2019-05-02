from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Post(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=User,
                               on_delete=models.SET_NULL,
                               null=True)
    likes = models.ManyToManyField(to=User,
                                   related_name='likes',
                                   blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(to='Tag',
                                 related_name = 'tags',
                                 blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:chat_page', args=[self.id])

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    post = models.ForeignKey(to=Post,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE)
    reply = models.ForeignKey(to='Comment', null=True, related_name='replies', on_delete=models.SET_NULL)
    content = models.TextField(max_length=1500)
    timestap = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name