from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Watch It")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    """This will delete all of users' posts"""
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
        """This will allow us to see title and author on admin page"""
