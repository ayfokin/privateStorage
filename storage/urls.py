from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'([0-9]|[a-z]|[A-Z]){11}', views.get_from_storage)
]