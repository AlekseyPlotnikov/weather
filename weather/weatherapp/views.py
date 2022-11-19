from django.shortcuts import render
import requests

from weatherapp.models import City


def index(request):
    appid = '5ad1dfc918bfd06bd401fa4b21db0748'
    url = ' https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
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
    context = {'all_info': all_cities}
    return render(request, 'weather/index.html', context)
