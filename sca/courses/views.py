from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course/list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course/detail.html'

