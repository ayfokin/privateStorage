# Generated by Django 3.2.4 on 2021-06-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='create_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]