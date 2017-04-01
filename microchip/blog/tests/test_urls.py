from django.core.urlresolvers import resolve
from django.test import TestCase
from blog.views import get_posts, authenticate, index

class UrlTest(TestCase):
    def test_can_resolve_get_posts(self):
        found = resolve('/get_posts/')
        self.assertEqual(found.func, get_posts)

    def test_can_resolve_login(self):
        found = resolve('/login/')
        self.assertEqual(found.func, authenticate)

    def test_can_resolve_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
