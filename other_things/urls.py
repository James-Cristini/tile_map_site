from django.conf.urls import url
from . import views

app_name='other_things'

urlpatterns = [
    # /other_things/
    url(r'^$', views.splash, name='splash'),

    # /other_things/home/
    url(r'^home/$', views.home, name='home'),

    # other_things/1/
    url(r'^(?P<image_id>[0-9]+)/$', views.detail, name='detail'),
    ]
