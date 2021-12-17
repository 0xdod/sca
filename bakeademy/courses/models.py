import os

from django.core.files import File
from django.db import models
from django.conf import settings
from django.urls.base import reverse
from django.utils.text import slugify

from bakeademy.core.models import TimestampedModel

# Create your models here.


class Course(TimestampedModel):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/', blank=True)
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="courses", )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        index_together = [
            ("id", "slug"),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.image:
            filepath = settings.BASE_DIR / 'static' / 'images' / 'no_image.png'
            self.image.save(
                os.path.basename(filepath),
                File(open(filepath, 'rb'))
            )

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('courses:detail', args=[self.pk, self.slug])


class Lesson(TimestampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='lessons')
    video_url = models.URLField()
    position = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.position}. {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('courses:lesson_detail', args=[self.course.pk, self.pk, self.slug])
