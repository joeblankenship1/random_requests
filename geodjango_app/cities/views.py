from django.views.generic import DetailView
from .models import City


class CitiesDetailView(DetailView):
    template_name = 'cities/city-detail.html'
    model = City
