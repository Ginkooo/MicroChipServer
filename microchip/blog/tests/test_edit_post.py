from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Post, Content
from blog.views import delete_post
from datetime import datetime
import json
import sys

class EditPostTest(TestCase):

    def setUp(self):

        Post.objects.all().delete()
        Content.objects.all().delete()

        date1 = datetime.now()
        date2 = datetime.now()
        date3 = datetime.now()
        date1 = date1.replace(year=2017, month=12)
        date2 = date2.replace(year=2017, month=11)
        date3 = date3.replace(year=2017, month=10)
        content1 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 1',
                english_content='Some english content for post 1', polish_link='polski-link-1', english_link='english-link-1')
        self.deleted_content = content2 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 2',
                        english_content='Some english content for post 2', polish_link='polski-link-2', english_link='english-link-2')
        content3 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 3',
                        english_content='Some english content for post 3', polish_link='polski-link-3', english_link='english-link-3')

        Post.objects.create(content=content1, author='durpal', category='cats', date=date1)
        self.post = Post.objects.create(content=content2, author='bartek', category='cats', date=date2)
        Post.objects.create(content=content3, author='piotr', category='snakes', date=date3)

        User.objects.all().delete()
        User.objects.create_user('bunny', 'some@mail.pl', 'p455w0rd')

    def test_ajax_required(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd')
        response = c.post('/edit_post/', {'id': 5})
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('ajax' in content['text'])

    def test_can_edit_post(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd')
        response = c.post('/edit_post/', {'id': '2', 'english_content': 'edited english content'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertEqual('OK', content['status'])
        self.assertTrue('edited' in Post.objects.get(pk=2).content.english_content)

    def test_doesnt_add_posts(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd')
        response = c.post('/edit_post/', {'id': '2', 'english_content': 'edited english content'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertTrue(3 == Post.objects.count())

    def test_refuses_to_edit_with_bad_things(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd')
        response = c.post('/edit_post/', {'id': '2', 'polish_link': ''}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
