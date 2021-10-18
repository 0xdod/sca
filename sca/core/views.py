from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from ..courses.models import Course

# Create your views here.


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_courses"] = Course.objects.all()[:3]
        return context


class AboutView(TemplateView):
    template_name = "core/about.html"


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("core:message_sent")

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactMessageSentView(TemplateView):
    template_name = "core/message_sent.html"

@login_required
def dashboard(request):
    enrolled_courses = request.user.courses.all()
    recommended = Course.objects.all().exclude(id__in=enrolled_courses)
    context = {
    'enrolled_courses': enrolled_courses,
    'recommended_courses': recommended,
    }
    return render(request, 'core/dashboard.html', context)