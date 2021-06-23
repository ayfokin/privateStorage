import json

from django import forms
from django.http import Http404, HttpResponse
from django.shortcuts import render
from storage.models import Data

# Create your views here.

with open("config.json", "r") as config_file:
    domain = json.load(config_file)["domain"]


class PwdForm(forms.Form):
    pwd = forms.CharField(widget=forms.PasswordInput, required=True)


def get_from_storage(request, *args, **kwargs):
    if request.method == 'GET':
        try:
            Data.Entry.get(link=domain + request.path)
        except Data.DoesNotExist:
            raise Http404
        return render(request, "password.html", {'form': PwdForm()})
    if request.method == 'POST':
        try:
            element = Data.Entry.get(link=domain + request.path)
            form = PwdForm(request.POST)
            if form.is_valid():
                pwd = form.cleaned_data['pwd']
                if pwd == element.password:
                    return render(request, "image.html", {'image': element.picture})
                else:
                    return HttpResponse(reason="Wrong password")
        except Data.DoesNotExist:
            raise Http404
