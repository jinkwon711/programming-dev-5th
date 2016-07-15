import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',lnglat):
        raise forms.ValidationError('Invalid LngLat Type')

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    captured_time= models.DateTimeField(default=timezone.now)
    places = models.ManyToManyField('Place')
    players =models.ForeignKey('Player')
    Pokemon_type = models.CharField(max_length=10, default="unknown")
    def __str__(self):
        return "Pokemon: "+self.name

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
