import factory

from ..models import Course, Lesson


class CourseFactory(factory.Factory):
    class Meta:
        model = Course

    title = factory.Faker("sentence")
    price = 99.99
    overview = factory.Faker("paragraph")


class LessonFactory(factory.Factory):
    class Meta:
        model = Lesson

    title = factory.Faker("sentence")
    course = factory.SubFactory(CourseFactory)
    overview = factory.Faker("paragraph")
    order = factory.Faker('pyint', min_value=1, max_value=99)

