import pytest

from django.utils.text import slugify
from django.urls import reverse
# from django.core.files.uploadedfile import SimpleUploadedFile

from .factories import CourseFactory, LessonFactory

@pytest.mark.django_db
class TestCourseModel:
    def test_save(self):
        course = CourseFactory()
        course.save()

        assert course.slug == slugify(course.title)
        assert course.thumbnail is not None

    def test_str(self):
        course = CourseFactory()

        assert str(course) == course.title

    def get_absolute_url(self):
        course = CourseFactory()

        assert course.get_absolute_url == reverse('courses:detail', kwargs={'id': course.id, 'slug' :course.slug})


@pytest.mark.django_db
class TestLessonModel:
    # def test_save(self):
    #     simple_file = SimpleUploadedFile(
    #         "best_file.mp4",
    #         b'0xd0d'
    #         )

    #     lesson = LessonFactory(video=simple_file)
    #     lesson.course.pk = 1
    #     lesson.save()

    #     assert lesson.slug == slugify(lesson.title)
    #     assert lesson.url is not None

    def test_str(self):
        lesson = LessonFactory()

        assert str(lesson) == f"{lesson.order}. {lesson.title}"

    def get_absolute_url(self):
        lesson = LessonFactory()
       
        assert lesson.get_absolute_url == reverse('courses:lesson_detail', args=[lesson.course.id,
            lesson.course.slug,
            lesson.id,
            lesson.slug])
