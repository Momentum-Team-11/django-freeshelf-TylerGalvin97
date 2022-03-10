from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    URL = models.URLField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField('Genre', related_name='sorted_books')

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, blank=True, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Genre name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()