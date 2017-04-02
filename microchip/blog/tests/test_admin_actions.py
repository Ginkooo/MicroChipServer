from django.test import TestCase, Client
from django.http import HttpRequest
from blog.views import add_post
import json
import sys

class AdminTest(TestCase):
    def test_ajax_required_add(self):
        c = Client()
        response = c.post('/add_post/', {})
        content = json.loads(response.content)
        self.assertTrue('ajax' in content['text'])
        self.assertEquals(500, response.status_code)

    def test_rejects_adding_incomplete_post(self):
        request = HttpRequest()
        request.POST['title'] = 'some title'
        request.POST['content'] = 'Fsdfdsfsdfdsfsdf'
        request.POST['language'] = 'pl'
        request.is_ajax = lambda : True
        response = add_post(request)
        content = json.loads(response.content)
        self.assertEquals(500, response.status_code)
        self.assertTrue('incomplete' in content['text'])

    def test_rejects_invalid_post_content(self):
        request = HttpRequest()
        request.POST['title'] = 'some title'
        request.POST['content'] = 'Fsdfdsfsdfdsfsdf'
        request.POST['language'] = 'pl'
        request.POST['category'] = ''
        request.is_ajax = lambda : True
        response = add_post(request)
        content = json.loads(response.content)
        self.assertEquals(500, response.status_code)
        self.assertTrue('empty' in content['text'])

    def test_rejects_invalid_language(self):
        request = HttpRequest()
        request.POST['title'] = 'some title'
        request.POST['content'] = 'Fsdfdsfsdfdsfsdf'
        request.POST['language'] = 'de'
        request.POST['category'] = ''
        request.is_ajax = lambda : True
        response = add_post(request)
        content = json.loads(response.content)
        self.assertEquals(500, response.status_code)
        self.assertTrue('language' in content['text'])
