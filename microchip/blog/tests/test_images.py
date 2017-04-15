from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Image
import json


class ImageTests(TestCase):

    def test_can_upload_image(self):
        image = SimpleUploadedFile(
            'kitties.png', b'kitties_in_boxes', 'image/png')
        response = self.client.post(
            '/upload_image/', {'name': 'image', 'attachment': image, 'tags': ['orion', ]})
        content = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue('path' in content)
        self.assertTrue(content['url'])
        self.assertEqual(1, Image.objects.all().count())
        self.assertEqual(content['url'], Image.objects.all()[0].image.url)
