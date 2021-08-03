from django.core import mail


from ..forms import ContactForm


class TestContactForm:

    def test_send_email(self):
        form_data = {'name':'damilola dolor',
        'email': 'damiloladolor@gmail.com',
        'message': 'Hello, I just signed up.'}

        form = ContactForm(data=form_data)
        form.is_valid()

        form.send_email(form.cleaned_data)

        first_message =  mail.outbox[0]

        assert len(mail.outbox) == 1
        assert first_message.subject == 'New message from Savorcakes Academy'
        assert form_data['message'] in first_message.body
