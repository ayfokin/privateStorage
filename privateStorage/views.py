import json

from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django import forms

from storage.models import Data
from storage.backend import generate_sequence, get_image

# Create your views here.

with open("config.json", "r") as config_file:
    domain = json.load(config_file)["domain"]


class TextForm(forms.Form):
    text = forms.CharField(label='Введите текст', max_length=100, required=True)


def home(request, *args, **kwargs):
    if request.method == 'GET':
        form = TextForm()
        return render(request, "home.html", {'form': form})
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            pic = get_image(form.cleaned_data['text'])
            link = domain + '/storage/' + generate_sequence()
            password = generate_sequence()
            entry = Data(link=link, password=password, picture=pic)
            entry.save()
            return render(request, "response.html", {'link': link, 'password': password})
        return HttpResponseBadRequest(reason=form.errors)






