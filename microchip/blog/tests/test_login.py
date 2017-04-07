from django.test import TestCase
from blog.views import authenticate
from django.http import HttpRequest
from django.test import Client
from django.contrib.auth.models import User
from blog.views import logged_in
from unittest.mock import Mock
import json

class LoginTest(TestCase):

    def setUp(self):
        User.objects.create_user('bunny', 'some_email', 'P4SSw0rd')

    def test_ajax_required(self):
        c = Client()
        response = c.post('/login/', {})
        content = json.loads(response.content)
        self.assertTrue('ajax' in content['text'])
        self.assertEqual(500, response.status_code)

        c = Client()
        response = c.post('/logout/', {})
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('ajax' in content['text'])

        c = Client()
        response = c.post('/logout/', {})
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('ajax' in content['text'])

    def test_can_login_user(self):
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

    def test_can_logout(self):
        c = Client()
        response = c.get('/logout/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual('OK', content['status'])

    def test_can_check_if_logged_in(self):
        request = Mock()
        request.is_ajax = Mock(return_value=True)
        user = Mock()
        user.is_authenticated = Mock(return_value=True)
        response = logged_in(request)
        content = json.loads(response.content)
        self.assertEquals('true', content['logged'])

