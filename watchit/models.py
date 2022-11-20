from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # reverse is a module of django
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    """This will delete all of users' posts"""
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
        """This will allow us to see title and author on admin page"""

    def get_absolute_url(self):
        return reverse('movie-detail', args=(str(self.id)))
        """self.id is similar to pk, we're asking it to go to itself,
        once the form has been submitted"""
        # This is if you want to return home /return reverse('home')

