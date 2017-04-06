
from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
from blog.models import Post, Content, Comment
import blog.views as views
from datetime import datetime
import json
import sys

class CommentTest(TestCase):
    def setUp(self):
        Content.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()
        date1 = datetime.now()
        date2 = datetime.now()
        date3 = datetime.now()
        date1 = date1.replace(year=2017, month=12)
        date2 = date2.replace(year=2017, month=11)
        date3 = date3.replace(year=2017, month=10)
        content1 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 1',
                english_content='Some english content for post 1', polish_link='polski-link-1', english_link='english-link-1')
        content2 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 2',
                        english_content='Some english content for post 2', polish_link='polski-link-2', english_link='english-link-2')
        content3 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 3',
                        english_content='Some english content for post 3', polish_link='polski-link-3', english_link='english-link-3')

        post1 = Post.objects.create(content=content1, author='durpal', category='cats', date=date1)
        post2 = Post.objects.create(content=content2, author='bartek', category='cats', date=date2)
        post3 = Post.objects.create(content=content3, author='piotr', category='snakes', date=date3)

        comment1 = Comment.objects.create(content='What an awesome post1!', author='Anonymous Blob1', post=post1, date=date1, parent_comment=None)
        comment2 = Comment.objects.create(content='What an awesome post2!', author='Anonymous Blob2', post=post2, date=date2, parent_comment=None)
        comment3 = Comment.objects.create(content='What an awesome post3!', author='Anonymous Blob3', post=post3, date=date3, parent_comment=None)
        comment4 = Comment.objects.create(content='What an awesome post1!', author='Anonymous Girl1', post=post1, date=date1, parent_comment=comment1)
        comment5 = Comment.objects.create(content='What an awesome post2!', author='Anonymous Girl2', post=post2, date=date2, parent_comment=None)
        comment6 = Comment.objects.create(content='What an awesome post3!', author='Anonymous Girl3', post=post3, date=date3, parent_comment=None)
        comment7 = Comment.objects.create(content='What an awesome post1!', author='Anonymous Dwarf', post=post1, date=date1, parent_comment=None)
        comment8 = Comment.objects.create(content='What an awesome post2!', author='Anonymous Boy', post=post1, date=date2, parent_comment=comment1)
        comment9 = Comment.objects.create(content='What an awesome post3!', author='Anonymous Musk', post=post3, date=date3, parent_comment=None)

    def test_can_get_comments_for_post(self):
        c = Client()
        response = c.post('/get_comments_for_post/', {'id': '1'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        content = json.loads(response.content)
        self.assertEqual(2, len(content['comments']))
        self.assertEqual(8, content['comments'][0]['subcomments'][1]['id'])
