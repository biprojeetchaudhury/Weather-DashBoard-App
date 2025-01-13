from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# API configuration
API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'City name is required'}), 400

    try:
        # Make the API request
        response = requests.get(WEATHER_API_URL, params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        })

        if response.status_code == 404:
            return jsonify({'error': 'City not found'}), 404
        elif response.status_code != 200:
            return jsonify({'error': 'Failed to fetch weather data'}), 500

        data = response.json()
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'condition': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }

        return jsonify(weather_data)

    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)

