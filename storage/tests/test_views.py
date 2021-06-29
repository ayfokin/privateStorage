from django.core.files.images import ImageFile
from django.test import TestCase
from storage.backend import generate_sequence
from storage.models import Data


class BackendTests(TestCase):
    def test_generate_sequence_length(self):
        string = generate_sequence()
        self.assertEquals(len(string), 11)


class PrivateStorageViewTests(TestCase):
    def test_view_index_get(self):
        resp = self.client.get('')
        self.assertEquals(resp.status_code, 200)
        self.assertTrue('form' in resp.context)
        self.assertTemplateUsed("/templates/index.html")

    def test_view_index_post_valid(self):
        resp = self.client.post('', data={'text': "zxc"})
        self.assertEquals(resp.status_code, 200)
        self.assertTrue('link' in resp.context)
        self.assertTrue('password' in resp.context)
        self.assertTemplateUsed("/templates/response.html")

    def test_view_index_post_invalid(self):
        resp = self.client.post('', data={'text': ""})
        self.assertEquals(resp.status_code, 400)


class StorageViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        with open('D:\\Study\\privateStorage\\media\\images\\test.png', 'r+b') as f:
            Data.Entry.create(link="http://127.0.0.1:8000/storage/qwertyuiop1",
                              password="1234567890A",
                              picture=ImageFile(f, name="test.png"))

    def test_view_get_from_storage_get_valid(self):
        resp = self.client.get('/storage/qwertyuiop1')
        self.assertEquals(resp.status_code, 200)
        self.assertTrue('form' in resp.context)
        self.assertTrue('wrong_pwd' in resp.context)
        self.assertEquals(resp.context['wrong_pwd'], False)
        self.assertTemplateUsed("/templates/password.html")

    def test_view_get_from_storage_get_invalid(self):
        resp = self.client.get('/storage/zzzzzzz')
        self.assertEquals(resp.status_code, 404)

    def test_view_get_from_storage_post_valid(self):
        resp = self.client.post('/storage/qwertyuiop1', data={"pwd": "1234567890A"})
        self.assertEquals(resp.status_code, 200)
        self.assertTrue('image' in resp.context)
        self.assertTrue('days' in resp.context)
        self.assertTrue('hours' in resp.context)
        self.assertTrue('minutes' in resp.context)
        self.assertTrue('seconds' in resp.context)
        self.assertTemplateUsed("/templates/image.html")

    def test_view_get_from_storage_post_invalid(self):
        resp = self.client.post('/storage/qwertyuiop1', data={"pwd": "zzzzzz"})
        self.assertTrue(resp is None or resp.status_code == 200)
        self.assertTrue('form' in resp.context)
        self.assertTrue('wrong_pwd' in resp.context)
        self.assertEquals(resp.context['wrong_pwd'], True)
        self.assertTemplateUsed("/templates/password.html")
