from django.db import models
from users.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts')
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title
