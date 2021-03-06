# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pokemon.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captured_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lnglat', models.CharField(help_text='경도,위도 포맷으로 입력', max_length=50, validators=[pokemon.models.lnglat_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pokemon_type', models.CharField(default='unknown', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='capture',
            name='places',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Place'),
        ),
        migrations.AddField(
            model_name='capture',
            name='players',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Player'),
        ),
        migrations.AddField(
            model_name='capture',
            name='pokemons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Pokemon'),
        ),
    ]
