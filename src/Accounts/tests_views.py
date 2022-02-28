from django.test import TestCase, Client

class HomePageTestCase(TestCase):
    def test_response_code_register(self):
        c = Client()
        response = c.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
    def test_response_code_login(self):
        c = Client()
        response = c.get('/accounts/login')
        self.assertEqual(response.status_code, 200)