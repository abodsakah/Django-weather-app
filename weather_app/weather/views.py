from django.shortcuts import render, HttpResponse
import requests

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e1f20849bd144d395d1f4009097c5239'
    city = 'valdemarsvik'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}

    return render(request, 'weather/index.html', context)
