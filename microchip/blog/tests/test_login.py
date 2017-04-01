from django.test import TestCase
from blog.views import authenticate
from django.test import Client
from django.contrib.auth.models import User
import json

class LoginTest(TestCase):
    
    def test_can_login_user(self):
        User.objects.create_user('bunny', 'some@email.com', 'P4SSw0rd')
        c = Client()
        response = c.post('/login/', {'username': 'bunny', 'password': 'P4SSw0rd'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual('OK', content['status'])

    def test_cannot_login_if_no_user(self):
        c = Client()
        response = c.post('/login/', {'username' : 'unexisting', 'password' : 'P4SSw0rd'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('invalid' in content['text'])
