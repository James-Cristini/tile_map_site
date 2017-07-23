from django.conf.urls import url
from . import views
from accounts.views import login_view, register_view, logout_view

app_name='tile_map'

urlpatterns = [
    # /tile_map/
    url(r'^home/$', views.tile_index, name='tile_index'),

    #tile_map/home/
    url(r'^$', views.tile_splash, name='tile_splash'),

    #tile_map/about/
    url(r'^faqs_page/$', views.faqs_page, name='faqs_page'),

    #tile_map/world_info/
    url(r'^world_info/$', views.world_info, name='world_info'),

    # /tile_map/1/
    url(r'^(?P<tile_id>[0-9]+)/$', views.tile_detail, name='tile_detail'),

    # /tile_map/world_info/people/1/
    url(r'^world_info/people/(?P<person_id>[0-9]+)/$', views.person_detail, name='person_detail'),
    # /tile_map/world_info/places/1/
    url(r'^world_info/places/(?P<place_id>[0-9]+)/$', views.place_detail, name='place_detail'),
    # /tile_map/world_info/organizations/1/
    url(r'^world_info/organizations/(?P<organization_id>[0-9]+)/$', views.organization_detail, name='organization_detail'),
    # /tile_map/world_info/people/1/
    url(r'^world_info/works/(?P<work_id>[0-9]+)/$', views.work_detail, name='work_detail'),
    # /tile_map/world_info/people/1/
    url(r'^world_info/tradegoods/(?P<tradegood_id>[0-9]+)/$', views.tradegood_detail, name='tradegood_detail'),
    # /tile_map/world_info/people/1/
    url(r'^world_info/cultures/(?P<culture_id>[0-9]+)/$', views.culture_detail, name='culture_detail'),

    # TODO make this map page a more dynamic zoomable image
    # /tile_map/full_map
    url(r'^full_map$', views.full_map, name='full_map'),


    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
]
