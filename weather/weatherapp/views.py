from django.shortcuts import render
import requests
from .forms import CityForm

from weatherapp.models import City


def index(request):
    appid = '5ad1dfc918bfd06bd401fa4b21db0748'
    url = ' https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_ifo = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_ifo)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
