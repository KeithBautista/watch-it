from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # reverse is a module of django
from datetime import datetime, date
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    """This will delete all of users' posts"""
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Action')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
        """This will allow us to see title and author on admin page"""

    def get_absolute_url(self):
        return reverse('movie-detail', args=(str(self.id)))
        """self.id is similar to pk, we're asking it to go to itself,
        once the form has been submitted"""
        # This is if you want to return home /return reverse('home')


