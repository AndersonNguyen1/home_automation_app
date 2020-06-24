from keys import city, state, weather_key
from datetime import date, datetime, time, timedelta
import requests

# def get_weather_details():
#     temp, weather, wind_speed = 'null', 'null', 'null'

#     if response.ok:
#         weather_data_total = len(response.json()["list"])
#         dt = response.json()["list"][weather_data_total - 1]["dt"]
#         temp = response.json()["list"][weather_data_total - 1]["main"]["temp"]
#         weather = response.json()["list"][weather_data_total - 1]["weather"][0]["main"]
#         wind_speed = response.json()["list"][weather_data_total - 1]["wind"]["speed"]
    
#     print(datetime.fromtimestamp(dt).strftime("%A, %B %d, %Y %I:%M:%S"))
#     print(weather_data_total)
#     print(temp)
#     print(weather)
#     print(wind_speed)

class Weather():
    def __init__(self):
        self.today = {}
        self.tomorrow = {}
        # p2 = plus 2
        self.today_p2 = {}
        self.today_p3 = {}
        self.date = date.today()
        self.time = time(15, 0, 0, 0)

    def get_data(self, key, city, state):
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state}&units=imperial&appid={key}')
        print(response.json()["list"])

if __name__ == "__main__":
    weather = Weather()
    weather.get_data(weather_key, city, state)
