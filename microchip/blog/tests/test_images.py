from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Image
import json


class ImageTests(TestCase):

    def setUp(self):
        image1 = Image()
        image1.image_file = SimpleUploadedFile(
            name='image1.png', content=b'content1', content_type='image/png')
        image1.full_clean()
        image1.save()
        image1.tags.add('tag1', 'tag2')

        image2 = Image()
        image2.image_file = SimpleUploadedFile(
            name='image2.png', content=b'content2', content_type='image/png')
        image2.full_clean()
        image2.save()
        image2.tags.add('tag2')

        image3 = Image()
        image3.image_file = SimpleUploadedFile(
            name='image3.png', content=b'content3', content_type='image/png')
        image3.full_clean()
        image3.save()
        image3.tags.add('tag3', 'tag1')

    def test_can_upload_image(self):
        Image.objects.all().delete()
        image = SimpleUploadedFile(
            'kitties.png', b'kitties_in_boxes', 'image/png')
        response = self.client.post(
            '/upload_image/', {'image': image, 'tags': ['orion', ]})
        content = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue('url' in content)
        self.assertTrue(content['url'])
        self.assertEqual(1, Image.objects.all().count())
        self.assertEqual(content['url'], Image.objects.all()[0].image_file.url)

    def test_can_return_images_by_tags(self):
        response = self.client.post('/get_images/', {'tags': ['tag3', 'tag1']})
        content = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(content['images']))
        self.assertEqual(1, content['images'][0]['id'])
        self.assertEqual(3, content['images'][1]['id'])

    def test_can_return_image_by_id(self):
        response = self.client.post('/get_images/', {'id': 2})
        content = json.loads(response.content)
        print(content)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(content['images']))
        self.assertEqual(2, content['images'][0]['id'])

    def test_can_return_image_by_post_id(self):
        response = self.client.post('/get_images/', {'id': 2})
        content = json.loads(response.content)
        print(content)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(content['images']))
        self.assertEqual(2, content['images'][0]['id'])
