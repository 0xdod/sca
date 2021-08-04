from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        subject = "New message from Savorcakes Academy"
        from_email = "admin@webhost.com"
        message = (
            "You have received a new message from your site "
            f"Savorcakes Academy from {name}, with the following email {email}\n\n"
        )
        message += self.cleaned_data.get("message")
        return send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[email],
        )
