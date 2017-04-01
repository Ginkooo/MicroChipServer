from django.test import TestCase
from blog.views import login
from django.test import Clinet
from django.contrib.auth.models import User
import json

class LoginTest(TestCase):
    
    def test_can_login_user(self):
        User.objects.create_user('bunny', 'some@email.com', 'P$SSw0rd')
        c = Client()
        response = client.post('/login', {'login' : 'bunny', 'password' : 'p4SSw0rd'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual('OK', content['status'])
