# weather_app/utils.py

import requests

def get_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': 'e6237d21ffd3d53e49717abcf37ecfb8', 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    return weather_data
