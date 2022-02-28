from django.test import TestCase, Client

class HomePageTestCase(TestCase):
    def test_response_code(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)