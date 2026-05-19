from django.db import models
from django.utils.text import slugify


class Method(models.Model):
    name = models.CharField(max_length=50, verbose_name='Method')
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(
        blank=True, verbose_name='Description of the tactic')
    image = models.ImageField(upload_to='methods/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Fish(models.Model):
    name = models.CharField(max_length=50, verbose_name='Fish kind')

    class Meta:
        verbose_name_plural = 'Fishes'

    def __str__(self): return self.name


class FishingPlace(models.Model):
    PLACE_TYPES = [
        ('river', 'river'),
        ('lake', 'lake'),
        ('swamp', 'swamp'),
    ]

    name = models.CharField(max_length=100, verbose_name='Object')
    slug = models.SlugField(unique=True, blank=True)
    place_type = models.CharField(
        max_length=10, choices=PLACE_TYPES, verbose_name='Type of reservoir')
    region = models.CharField(
        max_length=10, default='Pleven', verbose_name='Region')
    description = models.TextField(verbose_name='Info for location')
    image = models.ImageField(upload_to='places/', verbose_name='Picture')

    methods = models.ManyToManyField(
        Method, related_name='places', verbose_name='Appropriate methods')
    fishes = models.ManyToManyField(
        Fish, related_name='places', verbose_name='Types of fish here')
    map_embed = models.TextField(
        blank=True,
        null=True,
        verbose_name='Google Maps Embed Code',
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, help_text='Latitude')
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, help_text='Longitude')
    ACCESS_TYPES = [
        ('free', 'Свободен достъп (с билет)'),
        ('paid', 'Платен обект (такса)'),
    ]
    access_type = models.CharField(
        max_length=10,
        choices=ACCESS_TYPES,
        default='free',
        verbose_name='Access type'
    )
    is_recommended = models.BooleanField(
        default=False,
        verbose_name='Recommended Spot (Top 5)'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_place_type_display()})"
