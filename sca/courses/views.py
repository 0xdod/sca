from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect

from .models import Course, Lesson

# Create your views here.


class CourseListView(ListView):

    model = Course
    template_name = 'courses/course/list.html'


class CourseDetailView(DetailView):

    model = Course
    template_name = 'courses/course/detail.html'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'courses/lesson/detail.html'


def buy_course(request, c_id=None):

    if request.method == 'POST':
        payment_info = {
            'payment_for': 'course',
            'course_id': c_id,
            'title': 'Purchase course',
            'description': 'payment for online course at savorcakes academy', }

        request.session['payment_info'] = payment_info
        request.session.modified = True
        # user = request.user
        # user.enroll(course)
        return redirect('payments:process')
