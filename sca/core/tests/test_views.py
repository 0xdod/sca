from django.urls import reverse
from django.core import mail


from sca.testutils import SimpleTestCase




class TestIndexView(SimpleTestCase):

    def test_statusOK(self):
        self.get_check_200(reverse('core:index'))


class TestAboutView(SimpleTestCase):

    def test_statusOK(self):
        self.get_check_200(reverse("core:about"))


class TestContactView(SimpleTestCase):
    # test POST request, success email is sent, failure no email is sent

    def test_statusOK(self):
        self.get_check_200(reverse("core:contact"))


    def test_post(self):

        '''Test that form redirects to message:sent page on successful POST'''

        data = {
            "name": "Lorem ipsum",
            "email": "email@hey.com",
            "message": "lorem ipsum",
        }
        resp = self.client.post(reverse("core:contact"), data=data)

        assert len(mail.outbox) == 1
        assert data["message"] in mail.outbox[0].body
        assert resp.status_code == 302
        assert resp.get('Location') == reverse('core:message_sent')


class TestContactMessageSentView(SimpleTestCase):

    def test_statusOK(self):
        self.get_check_200(reverse("core:message_sent"))
