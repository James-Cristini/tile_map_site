from django.conf.urls import url
from . import views

app_name='tile_map'

urlpatterns = [
    # /tile_map/
    url(r'^$', views.tile_index, name='tile_index'),

    # /tile_map/1/
    url(r'^(?P<tile_id>[0-9]+)/$', views.tile_detail, name='tile_detail'),

    # TODO make this map page a more dynamic zoomable image
    # /tile_map/full_map
    url(r'^full_map$', views.full_map, name='full_map'),
]
