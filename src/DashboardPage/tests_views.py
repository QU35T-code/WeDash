from django.test import TestCase, Client

# Views tests here !

class DashboardPageTestCase(TestCase):
    def test_response_code(self):
        c = Client()
        response = c.get('/dashboard', follow=True)
        self.assertEqual(response.status_code, 200)
