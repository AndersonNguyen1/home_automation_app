from keys import weather_key, state, city
import requests
print(f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state}&appid={weather_key}')
response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state}&appid={weather_key}')

print(response)