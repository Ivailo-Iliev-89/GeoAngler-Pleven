from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from fishing_app.models import FishingPlace


class Post(models.Model):
    TYPE_OF_CHOICES = [
        ('0', "Draft"),
        ('1', 'Publish'),
    ]
    location = models.ForeignKey(
        FishingPlace, on_delete=models.CASCADE, related_name='posts', verbose_name='Location')
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='blog_images/',
                              verbose_name='Picture of fishing spot')
    content = models.TextField(verbose_name='Tell me about the adventure')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.TextField(choices=TYPE_OF_CHOICES, default=1)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, ** kwargs)

    def __str__(self):
        return self.title
