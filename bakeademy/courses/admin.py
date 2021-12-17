from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Course, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    prepopulated_fields = {"slug": ("title", )}


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created_at"]
    prepopulated_fields = {"slug": ("title", )}
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "slug"]
    prepopulated_fields = {"slug": ("title", )}
