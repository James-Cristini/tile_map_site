from django.shortcuts import render, get_object_or_404
from .models import Tile
from tile_logic import get_matrix

def tile_index(request):
    all_tiles = Tile.objects.all()
    tile_matrix = get_matrix(Tile.objects.all())
    # return HttpResponse("<h1>Tile Map home page!</h1>")
    return render(request, 'tile_map/tile_index.html', {'all_tiles':all_tiles, "tile_matrix":tile_matrix})

def tile_detail(request, tile_id):
    tile = get_object_or_404(Tile, id=tile_id)
    all_tiles = Tile.objects.all()
    max_id = max(x.id for x in all_tiles)
    next_id = int(tile_id) + 1
    previous_id = int(tile_id) - 1
    print "MAX", max_id
    return render(request,  'tile_map/tile_detail.html', {'Tile': tile, "max_id":max_id, "next_id":next_id, "previous_id":previous_id})

def full_map(request):
    return render(request, 'tile_map/full_map.html')

def get_query(request):
    filtered = []
    return render(request, )
