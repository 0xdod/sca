import pytest

from django.utils.text import slugify

from .factories import CourseFactory

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
