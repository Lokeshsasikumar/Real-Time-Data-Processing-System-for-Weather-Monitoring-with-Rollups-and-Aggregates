import time
import requests
from database import store_weather_data, store_daily_summary
from config import API_KEY, CITIES, INTERVAL, TEMP_UNIT
from api_service import get_weather_data, kelvin_to_celsius, kelvin_to_fahrenheit

def process_weather_data():
    while True:
        for city in CITIES:
            data = get_weather_data(city, API_KEY)
            if data:
                temperature_k = data['main']['temp']
                if TEMP_UNIT == 'Celsius':
                    temperature = kelvin_to_celsius(temperature_k)
                else:
                    temperature = kelvin_to_fahrenheit(temperature_k)

                weather_data = {
                    'city': city,
                    'temperature': temperature,
                    'feels_like': data['main']['feels_like'],
                    'weather_condition': data['weather'][0]['main'],
                    'timestamp': data['dt']
                }
                store_weather_data(weather_data)
        time.sleep(INTERVAL)

if __name__ == '__main__':
    process_weather_data()
