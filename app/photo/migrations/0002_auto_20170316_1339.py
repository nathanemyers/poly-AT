# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field='height', upload_to='static/tmp', width_field='width'),
        ),
    ]
