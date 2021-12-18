from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import View, TemplateView

from .models import Course, Lesson

# Create your views here.


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'


class LessonView(TemplateView, View):
    template_name = 'courses/lesson_detail.html'
    course = None
    lesson = None

    def get(self, request, course_id, pk, slug):
        return super().get(request, course_id, pk, slug)

    def dispatch(self, request, *args, **kwargs):
        self.course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        self.lesson = get_object_or_404(Lesson, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        context['lesson'] = self.lesson
        return context
