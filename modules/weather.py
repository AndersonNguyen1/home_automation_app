from modules.keys import weather_key, state, city
import requests

def get_weather_details():
    temp, weather, wind_speed = 'null', 'null', 'null'

    response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state}&appid={weather_key}')

    if response.ok:
        temp = response.json()["list"][0]["main"]["temp"]
        weather = response.json()["list"][0]["weather"][0]["main"]
        wind_speed = response.json()["list"][0]["wind"]["speed"]

    print(temp)
    print(weather)
    print(wind_speed)

