# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 03:49
from __future__ import unicode_literals

import blog.customfield
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160731_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zip_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=7, validators=[blog.validators.ZipCodeValidator2], verbose_name='우편번호')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.customfield.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='zipcode',
            field=models.CharField(max_length=7, validators=[blog.validators.ZipCodeValidator], verbose_name='우편번호'),
        ),
    ]