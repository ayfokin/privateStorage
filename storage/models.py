from django.db import models

# Create your models here.


class Data(models.Model):
    link = models.CharField(max_length=50)
    password = models.CharField(max_length=11)
    picture = models.ImageField()
    create_time = models.DateTimeField(auto_now_add=True)
    Entry = models.Manager()
