from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 'e6237d21ffd3d53e49717abcf37ecfb8'
weather_api_url = 'http://api.openweathermap.org/data/2.5/weather'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    response = requests.get(weather_api_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template('index.html', weather=weather_data)
    else:
        error_message = f"Error: {data['message']}"
        return render_template('error.html', error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
