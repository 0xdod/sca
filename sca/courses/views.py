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


def buy_course(request, id=None):
    
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=id)
        user = request.user
        user.enroll(course)

        return redirect('core:dashboard')
