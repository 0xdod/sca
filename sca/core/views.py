from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


from .forms import ContactForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'core/index.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:message_sent')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactMessageSentView(TemplateView):
    template_name = 'core/message_sent.html'

