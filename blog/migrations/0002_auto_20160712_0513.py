# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 05:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='lnalat',
            new_name='lnglat',
        ),
    ]
