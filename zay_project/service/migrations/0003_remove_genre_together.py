# Generated by Django 3.2 on 2021-05-07 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210507_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='together',
        ),
    ]