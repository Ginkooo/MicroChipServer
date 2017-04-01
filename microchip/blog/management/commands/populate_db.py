from django.core.management.base import BaseCommand
from blog.models import Post, Content
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
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
