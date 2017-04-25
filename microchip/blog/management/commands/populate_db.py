from django.core.management.base import BaseCommand
from blog.models import Post, Content, Comment
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
                english_content='Some english content for post 1', english_title='Some elglish title dor post 1', polish_title='Some polish title for post 1', polish_link='polski-link-1', english_link='english-link-1')
        content2 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 2',
                        english_content='Some english content for post 2', english_title='Some elglish title dor post 2', polish_title='Some polish title for post 1', polish_link='polski-link-2', english_link='english-link-2')
        content3 = Content.objects.create(polish_content='Jakiś tam polski kontent dla posta 3',
                        english_content='Some english content for post 3', english_title='Some elglish title dor post 3', polish_title='Some polish title for post 3', polish_link='polski-link-3', english_link='english-link-3')

        post1 = Post.objects.create(content=content1, author='durpal', category='spacecrafts', date=date1)
        post2 = Post.objects.create(content=content2, author='bartek', category='cats', date=date2)
        post3 = Post.objects.create(content=content3, author='piotr', category='snakes', date=date3)

        comment1 = Comment.objects.create(post=post1, author='SomeAuthor',content='Some content in comment 1', parent_comment=None, date=date1)
        comment2 = Comment.objects.create(post=post1, author='Maciej',content='Some content in comment 2', parent_comment=comment1, date=date2)
        comment3 = Comment.objects.create(post=post1, author='Durpal',content='Some content in comment 3', parent_comment=None, date=date3)
