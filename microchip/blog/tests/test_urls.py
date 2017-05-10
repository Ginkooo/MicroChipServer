from django.core.urlresolvers import resolve
from django.test import TestCase
from blog.views import get_posts, authenticate, index, logout, add_post, delete_post, edit_post, get_comments_for_post, logged_in, delete_comment, upload_image, get_images, delete_image, create_contact, is_contact_filled, get_contact_info, edit_contact_info, get_post, show_post


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

    def test_can_logout(self):
        found = resolve('/logout/')
        self.assertEqual(found.func, logout)

    def test_can_resolve_add_post(self):
        found = resolve('/add_post/')
        self.assertEqual(found.func, add_post)

    def test_can_resolve_delete_post(self):
        found = resolve('/delete_post/')
        self.assertEqual(found.func, delete_post)

    def test_can_resolve_edit_post(self):
        found = resolve('/edit_post/')
        self.assertEqual(found.func, edit_post)

    def test_can_resolve_get_comments(self):
        found = resolve('/get_comments_for_post/')
        self.assertEqual(found.func, get_comments_for_post)

    def test_can_resolve_logged_in(self):
        found = resolve('/logged_in/')
        self.assertEqual(found.func, logged_in)

    def test_can_resolve_delete_comment(self):
        found = resolve('/delete_comment/')
        self.assertEqual(found.func, delete_comment)

    def test_can_resolve_upload_image(self):
        found = resolve('/upload_image/')
        self.assertEqual(found.func, upload_image)

    def test_can_resolve_get_images(self):
        found = resolve('/get_images/')
        self.assertEqual(found.func, get_images)

    def test_can_resolve_delete_image(self):
        found = resolve('/delete_image/')
        self.assertEqual(found.func, delete_image)

    def test_can_resolve_create_contact(self):
        found = resolve('/create_contact/')
        self.assertEqual(found.func, create_contact)

    def test_can_resolve_delete_image(self):
        found = resolve('/is_contact_filled/')
        self.assertEqual(found.func, is_contact_filled)

    def test_can_resolve_edit_contact(self):
        found = resolve('/edit_contact_info/')
        self.assertEqual(found.func, edit_contact_info)

    def test_can_resolve_get_contact_info(self):
        found = resolve('/get_contact_info/')
        self.assertEqual(found.func, get_contact_info)

    def test_can_resolve_get_post(self):
        found = resolve('/get_post/')
        self.assertEqual(found.func, get_post)

    def test_can_resolve_get_post(self):
        found = resolve('/post/sth')
        self.assertEqual(found.func, show_post)

