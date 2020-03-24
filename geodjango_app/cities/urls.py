from django.conf.urls import url
from . import views


app_name = 'cities'

urlpatterns = [
    url(r'^city/(?P<pk>[0-9]+)$',
        views.CitiesDetailView.as_view(), name='city-detail'),
]
