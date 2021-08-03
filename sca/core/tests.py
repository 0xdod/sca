from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class TestIndexView(SimpleTestCase):

    def test_statusOK(self):
        response = self.client.get(reverse('core:index'))
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('core:index'))
        self.assertTemplateUsed(response, 'core/index.html')

    def test_page_content(self):
        response = self.client.get(reverse('core:index'))
        self.assertContains(response, 'Hello world')

class TestAboutView(SimpleTestCase):

    def test_statusOK(self):
        response = self.client.get(reverse('core:about'))
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('core:about'))
        self.assertTemplateUsed(response, 'core/about.html')

    def test_page_content(self):
        response = self.client.get(reverse('core:about'))
        self.assertContains(response, 'About us')

