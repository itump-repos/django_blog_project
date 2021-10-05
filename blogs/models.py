from django.db import models
from django.urls import reverse

# Create your models here.

# Post - what fields should you have the database for Post


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        # need self - difference between function and a method -- method uses self
        # return str(self.title) - If you just want to use title
        # This changes to POST Title from the site  -- Adds the two fields
        return "{} {}".format(self.title, self.date_created)

    def get_absolute_url(self):
        return reverse('PostDetail', kwargs={'pk': self.pk})
