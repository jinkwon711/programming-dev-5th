# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 01:44
from __future__ import unicode_literals

import blog.customfield
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160801_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='zip_code',
            name='city',
            field=models.CharField(default='hi', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zip_code',
            name='dong',
            field=models.CharField(default='hi', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zip_code',
            name='gu',
            field=models.CharField(default='hi', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zip_code',
            name='road',
            field=models.CharField(default='hi', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.customfield.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='zip_code',
            name='zip_code',
            field=models.CharField(max_length=20),
        ),
    ]