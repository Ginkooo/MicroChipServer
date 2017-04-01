from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
from blog.models import Post, Content
import blog.views as views
from datetime import datetime
import json
import sys

class GetPostsTest(TestCase):
    def setUp(self):
        date1 = datetime.now()
        date2 = datetime.now()
        date3 = datetime.now()
        date1 = date1.replace(year=2017, month=12)
        date2 = date2.replace(year=2017, month=11)
        date3 = date3.replace(year=2017, month=10)
        content1 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 1',
                english_content='Some english content for post 1')
        content2 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 2',
                        english_content='Some english content for post 2')
        content3 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 3',
                        english_content='Some english content for post 3')

        Post.objects.create(content=content1, author='durpal', category='spacecrafts', date=date1)
        Post.objects.create(content=content2, author='bartek', category='cats', date=date2)
        Post.objects.create(content=content3, author='piotr', category='snakes', date=date3)

    def test_get_post_can_select_proper_language_for_posts(self):
        polish_request = HttpRequest()
        polish_request.is_ajax = lambda : True
        polish_request.GET['language'] = 'pl'

        english_request = HttpRequest()
        english_request.is_ajax = lambda : True
        english_request.GET['language'] = 'en'

        polish_response = views.get_posts(polish_request)
        english_response = views.get_posts(english_request)

        content = json.loads(polish_response.content)
        for post in content['posts']:
            self.assertTrue('polski' in post['content'])

        content = json.loads(english_response.content)
        for post in content['posts']:
            self.assertTrue('english' in post['content'])

    def test_can_select_given_amount_of_posts_query_string(self):
        c = Client()
        response = c.get('/get_posts/?count=2', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertTrue(2 == len(content['posts']))

