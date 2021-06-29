import json
from tempfile import TemporaryFile

from django.core.files.images import ImageFile
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django import forms

from storage.models import Data
from storage.backend import generate_sequence, create_image, optimize_db

# Create your views here.

with open("config.json", "r") as config_file:
    domain = json.load(config_file)["domain"]


class TextForm(forms.Form):
    text = forms.CharField(label='Enter secret information', max_length=100,
                           widget=forms.TextInput(attrs={'required': 'true'}))


def index(request, *args, **kwargs):
    # optimize_db(repeat=5)
    if request.method == 'GET':
        form = TextForm()
        return render(request, "index.html", {'form': form})
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            try:
                with TemporaryFile(mode='w+b') as tmp:
                    create_image(form.cleaned_data['text'], tmp)
                    link = domain + '/storage/' + generate_sequence()
                    password = generate_sequence()
                    entry = Data(link=link, password=password,
                                 picture=ImageFile(tmp, name=generate_sequence() + '.png'))
                    entry.save()
                    return render(request, "response.html", {'link': link, 'password': password})
            except:
                return HttpResponseServerError
        return HttpResponseBadRequest(reason=form.errors)
