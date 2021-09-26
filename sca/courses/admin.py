from django.contrib import admin

from .models import Course, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created_at"]
    prepopulated_fields = {"slug": ("title", )}
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["order", "title", "course", "slug"]
