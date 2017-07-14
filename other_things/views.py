from django.shortcuts import render, get_object_or_404
from .models import Image

def splash(request):
    return render(request, 'other_things/splash.html')

def home(request):
    image_list = Image.objects.all()
    return render(request, 'other_things/home.html', {"image_list":image_list})

def detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image_list = Image.objects.all()
    max_id = max(x.id for x in image_list)
    next_id = int(image_id) + 1
    previous_id = int(image_id) - 1
    return render(request, 'other_things/detail.html', {"image":image, "max_id":max_id, "next_id":next_id, "previous_id":previous_id})
