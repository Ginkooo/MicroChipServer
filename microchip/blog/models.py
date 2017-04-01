from django.db import models

# Create your models here.

class Content(models.Model):
    '''
    Entity contains content for according post, in multiple languages
    '''
    english_title = models.CharField(max_length=100)
    polish_title = models.CharField(max_length=100)
    english_content = models.TextField()
    polish_content = models.TextField()

class Post(models.Model):
    '''
    Its an entity reptesenting a single post. It's content is in 'Content' table
    '''
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateTimeField()
