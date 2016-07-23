from django.shortcuts import render
from pokemon.models import Pokemon, Player, Place, Capture

def pokemon_main(request):
    return render(request, 'pokemon/pokemon_main.html', {})

def pokemon_list(request):
    qs = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html',{
        'pokemon_list' : qs,
        })
def pokemon_detail(request, pk):
    qs = Pokemon.objects.get(pk=pk)
    return render(request, 'pokemon/pokemon_detail.html',{
        'pokemon_detail' :qs ,
        })

def player_list(request):
    qs = Player.objects.all()
    return render(request, 'pokemon/player_list.html',{
        'player_list' : qs,
        })

def player_detail(request, pk):
    qs = Player.objects.get(pk=pk)
    qs_capture = Capture.objects.filter(players__pk=pk)
    return render(request, 'pokemon/player_detail.html',{
        'player_detail' : qs ,
        'player_captured' :qs_capture,
        })
def capture_list(request):
    qs = Capture.objects.all()
    return render(request, 'pokemon/capture_list.html',{
        'capture_list' : qs,
        })
def capture_detail(request, pk):
    qs = Capture.objects.get(pk=pk)
    return render(request, 'pokemon/capture_detail.html',{
        'capture_detail' : qs,
        })
def place_list(request):
    qs = Place.objects.all()
    return render(request, 'pokemon/place_list.html',{
        'place_list' : qs,
        })
def place_detail(request, pk):
    qs = Place.objects.get(pk=pk)
    return render(request, 'pokemon/place_detail.html',{
        'place_detail' : qs,
        })