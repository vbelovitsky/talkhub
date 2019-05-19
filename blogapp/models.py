from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
                                 related_name='tags',
                                 blank=True)
    private = models.BooleanField(default=0)
    private_key = models.CharField(default='public', max_length=32)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:chat_page', args=[self.id, self.private_key])

    def is_private(self):
        return bool(self.private)

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


class Profile(models.Model):
    user = models.OneToOneField(to=User,
                                on_delete=models.CASCADE)
    country = models.CharField(max_length=32, blank=True)
    contacts = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to='images', blank=True)



