
from django.test import TestCase
from blog.models import Contact
import json


class ConcatTests(TestCase):

    def test_can_add_contact_when_no_contact(self):
        response = self.client.post('/create_contact/', {
            'phone': 555,
            'email': 'some@email.com',
            'address': 'House St. 1'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, Contact.objects.all().count())

    def test_cant_create_contact_if_there_is_one_already(self):
        Contact.objects.create(
            phone='423525', email='any@email.com', address='Some Address')
        response = self.client.post('/create_contact/', {
            'phone': '655555555',
            'email': 'dome@email.com',
            'address': 'Fouse St. 1'})
        self.assertEqual(500, response.status_code)
        self.assertEqual(1, Contact.objects.all().count())

    def test_cant_edit_contact(self):
        Contact.objects.create(
            phone='423525', email='any@email.com', address='Some Address')
        response = self.client.post('/edit_contact_info/', {
            'phone': '655'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, Contact.objects.all().count())
        self.assertEqual('655', Contact.objects.all()[0].phone)

    def test_get_contact_info(self):
        Contact.objects.create(
            phone='423525', email='any@email.com', address='Some Address')
        response = self.client.get('/get_contact_info/')
        content = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, Contact.objects.all().count())
        self.assertEqual('423525', Contact.objects.all()[0].phone)
        self.assertTrue('phone' in content and 'address' in content and 'email' in content)
        self.assertEqual(content['phone'], '423525')
