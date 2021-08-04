from django.test.client import Client


class SimpleTestCase:
    client = Client()

    def get_check_200(self, url: str):
        response = self.client.get(url)
        assert response.status_code == 200
