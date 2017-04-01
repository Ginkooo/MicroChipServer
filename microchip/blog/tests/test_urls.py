from django.core.urlresolvers import resolve
from django.test import TestCase
from blog.views import get_posts

class UrlTest(TestCase):
    def test_can_resolve_get_posts(self):
        found = resolve('/get_posts/')
        self.assertEqual(found.func, get_posts)
