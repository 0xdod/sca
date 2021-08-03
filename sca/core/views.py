from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'core/index.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(FormView):
    pass
