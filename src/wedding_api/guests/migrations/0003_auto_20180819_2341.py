# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-19 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_auto_20180819_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='name',
            new_name='full_name',
        ),
    ]
