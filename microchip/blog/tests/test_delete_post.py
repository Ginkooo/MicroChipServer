from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Post, Content
from blog.views import delete_post
from datetime import datetime
import json
import sys

class DeletePostTest(TestCase):

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

    def test_can_delete_post(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        c.post('/delete_post/', {'id': '2'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = c.post('/delete_post/', {'id': '1'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response_content = json.loads(response.content)
        self.assertEqual(1, Post.objects.count())
        self.assertEqual(1, Content.objects.count())
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(author='bartek')
        with self.assertRaises(Content.DoesNotExist):
            Content.objects.get(english_link='english-link-2')
        self.assertEquals('OK', response_content['status'])

    def test_cannot_make_non_ajax_connection(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        response = c.post('/delete_post/', {'id': self.post.id})
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('ajax' in content['text'])

    def test_login_required(self):
        c = Client()
        response = c.post('/edit_post/', {'id': '2', 'english_content': 'edited english content'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(200 != response.status_code)

    def test_cannot_delete_post_with_wrong_id(self):
        c = Client()
        c.login(username='bunny', password='p455w0rd'),
        response = c.post('/delete_post/', {'id': '50'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual(500, response.status_code)
        self.assertTrue('post' in content['text'])

