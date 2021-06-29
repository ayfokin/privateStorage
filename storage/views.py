import json
import math

import pytz
from django import forms
from django.http import Http404, HttpResponse, HttpResponseServerError
from django.shortcuts import render
from storage.models import Data
from datetime import datetime, timedelta

# Create your views here.

with open("config.json", "r") as config_file:
    domain = json.load(config_file)["domain"]


class PwdForm(forms.Form):
    pwd = forms.CharField(label='Enter password', max_length=20,
                          widget=forms.PasswordInput, required=True)


def get_from_storage(request, *args, **kwargs):
    if request.method == 'GET':
        try:
            Data.Entry.get(link=domain + request.path)
        except Data.DoesNotExist:
            raise Http404
        return render(request, "password.html", {'form': PwdForm(), 'wrong_pwd': False})
    if request.method == 'POST':
        try:
            element = Data.Entry.get(link=domain + request.path)
            form = PwdForm(request.POST)
            if form.is_valid():
                pwd = form.cleaned_data['pwd']
                if pwd == element.password:
                    now = pytz.utc.localize(datetime.utcnow())
                    delta = timedelta(days=7)
                    response = render(request, "image.html",
                                      {'image': element.picture,
                                       'days': math.floor((delta - (now - element.create_time)).days),
                                       'hours': math.floor((delta - (now - element.create_time)).seconds / 60 / 60),
                                       'minutes': math.floor((delta - (now - element.create_time)).seconds / 60 % 60),
                                       'seconds': math.floor((delta - (now - element.create_time)).seconds % 60)})
                    response.set_cookie("date", datetime.now().__str__())
                    response.set_cookie("r_path", request.path)
                    return response
                else:
                    return render(request, "password.html", {'form': PwdForm(), 'wrong_pwd': True})
        except Data.DoesNotExist:
            raise Http404
        except:
            return HttpResponseServerError
