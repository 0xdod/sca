from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserForm


class ProfileView(FormView):
    template_name = "account/profile.html"
    form_class = UserForm
    success_url = reverse_lazy("core:dashboard")


    def get_form(self):
        if self.request.method == "POST":
            return UserForm(data=self.request.POST, instance=self.request.user)

        return UserForm(instance=self.request.user)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Profile updated')

        return super().form_valid(form)
