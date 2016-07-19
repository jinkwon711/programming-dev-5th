from django.contrib import admin
from pokemon.models import Pokemon
from pokemon.models import Place
from pokemon.models import Player
from pokemon.models import Capture

class PokemonAdmin(admin.ModelAdmin):
    list_display = ["name","pokemon_type"]

class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "lnglat"]

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name"]

class CaptureAdmin(admin.ModelAdmin):
    list_display = ["pokemons","players","captured_time"]

# Register your models here.
admin.site.register(Pokemon,PokemonAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Capture, CaptureAdmin)