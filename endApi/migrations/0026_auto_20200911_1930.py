# Generated by Django 3.0.7 on 2020-09-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0025_auto_20200911_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]