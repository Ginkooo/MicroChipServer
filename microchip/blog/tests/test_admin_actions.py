from django.test import TestCase, Client
from django.http import HttpRequest
from django.contrib.auth.models import User
from blog.views import add_post
from blog.models import Post
import copy
import json
import sys

class AdminTest(TestCase):

    valid_post = dict()

    def setUp(self):
        User.objects.create_user('bunny', 'some@mail.pl', 'p455w0rd')

        self.valid_post['polish_title']='polish-title'
        self.valid_post['english_title']='english-title'
        self.valid_post['polish_content']='polish-content'
        self.valid_post['english_content']='english-content'
        self.valid_post['polish_link']='polish-link'
        self.valid_post['english_link']='english-link'
        self.valid_post['author']='Some author'
        self.valid_post['category']='Some category'

    def test_ajax_required_add(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        response = c.post('/add_post/', {})
        content = json.loads(response.content)
        self.assertTrue('ajax' in content['text'])
        self.assertEquals(500, response.status_code)

    def test_adds_valid_post(self):
        Post.objects.all().delete()
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        response = c.post('/add_post/', self.valid_post, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEquals(1, Post.objects.count())
        self.assertEqual('OK', content['status'])

    def test_cannot_add_post_with_no_link(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        post = copy.deepcopy(self.valid_post)
        post.pop('polish_link', None)
        response = c.post('/add_post/', post, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('polish_link' in content['text'])

    def test_cannot_add_post_with_empty_link(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        post = copy.deepcopy(self.valid_post)
        post['polish_link'] = ''
        response = c.post('/add_post/', post, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('polish_link' in content['text'])

    def test_can_add_post_with_no_english_content(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        post = copy.deepcopy(self.valid_post)
        post.pop('english_content', None)
        response = c.post('/add_post/', post, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        content = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue('OK' in content['status'])


