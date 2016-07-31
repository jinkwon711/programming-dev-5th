# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 07:06
from __future__ import unicode_literals

import blog.models
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160719_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=blog.models.PhoneNumberField(default='01045467082', max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Markdown 문법을 써주세요.', validators=[blog.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[blog.validators.MaxLengthValidator(100)], verbose_name='제목'),
        ),
    ]
