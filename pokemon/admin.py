from django.contrib import admin
from pokemon.models import Pokemon
from pokemon.models import Place
from pokemon.models import Player

class PokemonAdmin(admin.ModelAdmin):
    list_display = ["name","captured_time","players"]

class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "lnglat"]

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name"]

# Register your models here.
admin.site.register(Pokemon,PokemonAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Player, PlayerAdmin)