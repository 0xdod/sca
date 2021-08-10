import factory

from ..models import Course


class CourseFactory(factory.Factory):
    class Meta:
        model = Course

    title = "A new course"
    price = 99.99
    overview = 'A sample overview'
