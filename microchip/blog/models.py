from django.db import models
from django.db import models
from django.core.validators import MinLengthValidator
from taggit.managers import TaggableManager

# Create your models here.


class Content(models.Model):
    '''
    Entity contains content for according post, in multiple languages
    '''
    english_title = models.CharField(
        max_length=100, validators=[MinLengthValidator(3)])
    polish_title = models.CharField(
        max_length=100, validators=[MinLengthValidator(3)])
    english_content = models.TextField(blank=True, null=True)
    polish_content = models.TextField(blank=True, null=True)
    polish_link = models.CharField(
        max_length=60, unique=True, validators=[MinLengthValidator(3)])
    english_link = models.CharField(
        max_length=60, unique=True, validators=[MinLengthValidator(3)])

    class Meta:
        unique_together = ('polish_link', 'english_link')


class Post(models.Model):
    '''
    Its an entity reptesenting a single post. It's content is in 'Content' table
    '''
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, validators=[
                                MinLengthValidator(3)])
    author = models.CharField(max_length=50, validators=[
                              MinLengthValidator(3)])
    date = models.DateTimeField()


class Comment(models.Model):
    '''
    Entity representing post comments
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField()


class Image(models.Model):
    '''
    Entity containing images
    '''
    image_file = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    tags = TaggableManager()
