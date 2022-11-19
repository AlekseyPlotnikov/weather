from django.shortcuts import render
import requests


def index(request):
    appid = '5ad1dfc918bfd06bd401fa4b21db0748'
    url = ' https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'London'
    res = requests.get(url.format(city)).json()
    city_ifo = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }
    context = {'info': city_ifo}
    return render(request, 'weather/index.html', context)
