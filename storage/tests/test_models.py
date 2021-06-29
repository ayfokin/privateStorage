from django.test import TestCase

from storage.models import Data


class DataModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data.Entry.create(link="http://127.0.0.1/storage/qwertyuiop1",
                          password="1234567890A")

    def test_link_label(self):
        data = Data.Entry.get(id=1)
        field_label = data._meta.get_field('link').verbose_name
        self.assertEquals(field_label, 'link')

    def test_password_label(self):
        data = Data.Entry.get(id=1)
        field_label = data._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_picture_label(self):
        data = Data.Entry.get(id=1)
        field_label = data._meta.get_field('picture').verbose_name
        self.assertEquals(field_label, 'picture')

    def test_create_time_label(self):
        data = Data.Entry.get(id=1)
        field_label = data._meta.get_field('create_time').verbose_name
        self.assertEquals(field_label, 'create time')

    def test_link_max_length(self):
        data = Data.Entry.get(id=1)
        max_length = data._meta.get_field('link').max_length
        self.assertEquals(max_length, 50)

    def test_password_max_length(self):
        data = Data.Entry.get(id=1)
        max_length = data._meta.get_field('password').max_length
        self.assertEquals(max_length, 11)

    def test_picture_upload_to(self):
        data = Data.Entry.get(id=1)
        upload_to = data._meta.get_field('picture').upload_to
        self.assertEquals(upload_to, 'images/')

    def test_create_time_auto_now_add(self):
        data = Data.Entry.get(id=1)
        auto_now_add = data._meta.get_field('create_time').auto_now_add
        self.assertTrue(auto_now_add)

