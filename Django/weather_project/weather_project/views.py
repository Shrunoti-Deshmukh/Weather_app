# weather_app/views.py

from django.shortcuts import render
from .utils import get_weather_data

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        weather_data = get_weather_data(city)
        print(weather_data)
        return render(request, 'index.html', weather_data)
    return render(request, 'index.html')
