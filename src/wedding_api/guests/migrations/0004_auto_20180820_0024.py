# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_auto_20180819_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='full_name',
            new_name='name',
        ),
    ]