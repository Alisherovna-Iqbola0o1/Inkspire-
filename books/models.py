from django.db import models
from django.utils.text import slugify
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    synopsis = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    published_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    rating_average = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title