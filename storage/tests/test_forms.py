from django.test import TestCase

from storage.views import PwdForm
from privateStorage.views import TextForm


class PwdFormTest(TestCase):
    def test_pwd_label(self):
        form = PwdForm()
        self.assertEquals(form.fields['pwd'].label, 'Enter password')

    def test_pwd_max_length(self):
        form = PwdForm()
        self.assertEquals(form.fields['pwd'].max_length, 20)

    def test_pwd_required(self):
        form = PwdForm()
        self.assertTrue(form.fields['pwd'].required)


class TextFormTest(TestCase):
    def test_text_label(self):
        form = TextForm()
        self.assertEquals(form.fields['text'].label, 'Enter secret information')

    def test_text_max_length(self):
        form = TextForm()
        self.assertEquals(form.fields['text'].max_length, 100)