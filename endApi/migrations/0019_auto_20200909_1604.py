# Generated by Django 3.0.7 on 2020-09-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0018_auto_20200909_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='country',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
    ]
