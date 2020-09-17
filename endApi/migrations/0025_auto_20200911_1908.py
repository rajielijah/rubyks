# Generated by Django 3.0.7 on 2020-09-11 19:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0024_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]