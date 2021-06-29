from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.


class Data(models.Model):
    link = models.CharField(max_length=50)
    password = models.CharField(max_length=11)
    picture = models.ImageField(upload_to='images/')
    create_time = models.DateTimeField(auto_now_add=True)
    Entry = models.Manager()


@receiver(pre_delete, sender=Data)
def delete_image(sender, instance, **kwargs):
    if instance.picture:
        instance.picture.delete(False)
