# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 04:24
from __future__ import unicode_literals

import blog.customfield
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160803_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='picture', upload_to='upload/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.customfield.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
    ]
