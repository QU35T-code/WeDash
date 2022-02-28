from django.test import TestCase, Client
from django.contrib.auth.models import User

class SupportPageTestCase(TestCase):
    def setUp(self): 
       User.objects.create_user('homer', 'homer@simpson.net', 'simpson')
    def test_response_code_disconnected(self):
        c = Client()
        response = c.get('/support/')
        self.assertEqual(response.status_code, 302)
    def test_response_code_connected(self):
        login = self.client.login(username='homer', password='simpson')
        self.assertTrue(login)
        response = self.client.get('/support', follow=True)
        self.assertEqual(response.status_code, 200)