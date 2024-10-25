import requests

def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def kelvin_to_fahrenheit(kelvin_temp):
    return (kelvin_temp - 273.15) * 9/5 + 32
