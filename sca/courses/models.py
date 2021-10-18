from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings

from sca.core.models import TimeStampedModel


# Create your models here.
class Course(TimeStampedModel):
    STATUS_CHOICES = (
            ('published', 'Published'),
            ('draft', 'Draft'),
            )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    overview = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to="images/courses/",
        blank=True,
        default="no_image.png",
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
            default='draft')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='courses', through='UserCourse')

    def student_progress(self, user_id):
        return UserCourse.objects.get(course_id=self.pk, user_id=user_id).progress


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

    def get_absolute_url(self):
        return reverse('courses:detail', args=[self.id, self.slug])

class Lesson(TimeStampedModel):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(to=Course,
                               on_delete=models.CASCADE,
                               related_name="lessons")
    slug = models.SlugField(max_length=250)
    order = models.PositiveIntegerField()
    overview = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to="videos", null=True, blank=True)
    url = models.URLField("video url", blank=True)

    class Meta:
        index_together = [
            ("id", "slug"),
        ]
        ordering = ("order", )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.url:
            self.url = self.video.url

        super().save(args, kwargs)

    def __str__(self):
        return f"{self.order}. {self.title}"
    
    def get_absolute_url(self):
        return reverse('courses:lesson_detail', args=[self.course.id,
            self.course.slug, self.id, self.slug])


class UserCourse(models.Model):
    STATUS_CHOICES = (
            ('completed', 'Completed'),
            ('in_progress', 'In Progress'),
        )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    progress = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES,
            default='in_progress')
