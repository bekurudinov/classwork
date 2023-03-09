from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title
class Comment(models.Model):
    author = models.CharField(max_length=100)
    date = models.DateField()
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.author} {self.content}'

