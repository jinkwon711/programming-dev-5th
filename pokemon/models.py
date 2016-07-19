import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',lnglat):
        raise forms.ValidationError('Invalid LngLat Type')


class Capture(models.Model):
    players = models.ForeignKey('Player',)
    pokemons = models.ForeignKey('Pokemon')
    places = models.ManyToManyField('Place')
    captured_time= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "captured_by: " + self.captured_time.strftime('%Y-%m-%d %H:%M:%S')


class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    # attack = models.IntegerField(max_length=4)
    # defense = models.IntegerField(max_length=4)
    # evolveLevel = models.IntegerField(max_length=4)
    pokemon_type = models.CharField(max_length=10, default="unknown")
    # moves=models.CharField(max_length=20)

    def __str__(self):
        return "Pokemon: " + self.name


class Place(models.Model):
    name = models.CharField(max_length=50)
    lnglat = models.CharField(max_length=50,validators=[lnglat_validator], help_text="경도,위도 포맷으로 입력")

    def __str__(self):
        return "Place: "+self.name


class Player(models.Model):
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return "Player: "+self.name

