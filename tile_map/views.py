from django.shortcuts import render, get_object_or_404
from .models import Tile, FAQ, Person, Place, Organization, Tradegood, Culture, WorkOfArt
from tile_logic import get_matrix
import random

def tile_splash(request):
    return render(request, 'tile_map/tile_splash.html')

def tile_index(request):
    all_tiles = Tile.objects.all()
    tile_matrix = get_matrix(Tile.objects.all())
    return render(request, 'tile_map/tile_index.html', {'all_tiles':all_tiles, "tile_matrix":tile_matrix})


def tile_detail(request, tile_id):
    tile = get_object_or_404(Tile, id=tile_id)
    all_tiles = Tile.objects.all()
    max_id = max(x.id for x in all_tiles)
    next_id = int(tile_id) + 1
    previous_id = int(tile_id) - 1
    random_id = random.randrange(1, max_id+1)
    tile_loc = Place.objects.filter(name=tile.location)[0]
    tradegoods = tile.tradegoods.all()
    organizations = tile.organizations.all()
    relevant_places = tile.relevant_places.all()
    people = Person.objects.filter(tile=tile.title)
    cultures = []

    context = {
    'Tile': tile,
    "max_id":max_id,
    "next_id":next_id,
    "previous_id":previous_id,
    "random_id":random_id,
    "tile_loc":tile_loc,
    "tradegoods":tradegoods,
    "people":people,
    "organizations":organizations,
    "places":relevant_places,
    }
    return render(request,  'tile_map/tile_detail.html', context)

def faqs_page(request):
    all_questions = FAQ.objects.all()
    return render(request, 'tile_map/faq.html', {'all_questions':all_questions})

def world_info(request):
    context = {
    "all_persons" : Person.objects.all(),
    "all_places" : Place.objects.all(),
    "all_organizations" : Organization.objects.all(),
    "all_tradegoods" : Tradegood.objects.all(),
    "all_cultures" : Culture.objects.all(),
    "all_works_of_art" : WorkOfArt.objects.all(),
    }
    return render(request, 'tile_map/world_info.html', context)

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    tiles = place.tiles.all()
    try:
        parent_loc = Place.objects.filter(name=place.parent_location)[0]
    except IndexError:
        parent_loc = None
    sub_locations = Place.objects.filter(parent_location=place.name)
    people = Person.objects.filter(location=place.name)
    organizations = Organization.objects.filter(location=place.name)
    tradegoods = Tradegood.objects.filter(location=place.name)
    works = WorkOfArt.objects.filter(location=place.name)
    context = {
    "place" : place,
    "sub_locations" : sub_locations,
    "people" : people,
    "parent_loc" : parent_loc,
    "organizations" : organizations,
    "tradegoods" : tradegoods,
    "works" : works,
    "tiles" : tiles
    }
    return render(request, 'tile_map/world_info/place_detail.html', context)

def person_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    try:
        person_loc = Place.objects.filter(name=person.location)[0]
    except IndexError:
        person_loc = None
    try:
        tile = Tile.objects.filter(title=person.tile)[0]
    except IndexError:
        tile = None
    return render(request, 'tile_map/world_info/person_detail.html', {"person":person, "person_loc":person_loc, "tile":tile})

def organization_detail(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    return render(request, 'tile_map/world_info/organization_detail.html', {"organization":organization})

def work_detail(request, work_id):
    work = get_object_or_404(WorkOfArt, id=work_id)
    return render(request, 'tile_map/world_info/work_detail.html', {"work":work})

def tradegood_detail(request, tradegood_id):
    tradegood = get_object_or_404(Tradegood, id=tradegood_id)
    return render(request, 'tile_map/world_info/tradegood_detail.html', {"tradegood":tradegood})

def culture_detail(request, culture_id):
    culture = get_object_or_404(Culture, id=culture_id)
    return render(request, 'tile_map/world_info/culture_detail.html', {"culture":culture})

def full_map(request):
    return render(request, 'tile_map/full_map.html')
