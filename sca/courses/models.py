from django.db import models
from django.utils.text import slugify

from sca.core.models import TimeStampedModel


# Create your models here.
class Course(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    overview = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to="images/courses/",
        blank=True,
        default="no_image.png",
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        index_together = [
            ("id", "slug"),
        ]
        ordering = ("-created_at", )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Lesson(TimeStampedModel):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(to=Course,
                               on_delete=models.CASCADE,
                               related_name="lessons")
    slug = models.SlugField(max_length=250)
    order = models.PositiveIntegerField()
    overview = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        index_together = [
            ("id", "slug"),
        ]
        ordering = ("order", )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.order}. {self.title}"
