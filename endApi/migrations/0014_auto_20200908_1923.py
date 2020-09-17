# Generated by Django 3.0.7 on 2020-09-08 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('endApi', '0013_remove_profile_user_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]