from django.test import TestCase
from django.http import HttpRequest
from blog.models import Post, Content
import blog.views as views
from datetime import datetime
import json

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
        request = HttpRequest()
        request.is_ajax = lambda : True
        request.GET['language'] = 'pl'
        response = views.get_posts(request)
        content = json.loads(response.content)
        for post in content['posts']:
            self.assertTrue('polski' in post['content'])
