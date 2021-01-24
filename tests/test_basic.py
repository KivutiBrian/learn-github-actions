from main import app
from flask_testing import TestCase
import unittest

class BasicTest(TestCase):
    def create_app(self):
        return app

    def test_home(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about',content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_other_page(self):
        response = self.client.get('/a', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b'does not exist' in response.data)