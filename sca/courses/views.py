from django.views.generic.list import ListView

from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course/list.html'
