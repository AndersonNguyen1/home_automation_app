from keys import city, state, weather_key # add back module.keys if you want to run in app.py main()
from datetime import date, datetime, time, timedelta
import requests

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
        return self.organize_data(response, response.json()["list"])
    
    def organize_data(self, response, data):
        temp, weather, wind_speed = 'null', 'null', 'null'

        ## weather_data_total - 1 is the 40th day in 5day/3hr 
        if response.ok:
            weather_data_total = len(response.json()["list"])
            dt = response.json()["list"][0]["dt"]
            temp = response.json()["list"][weather_data_total - 1]["main"]["temp"]
            weather = response.json()["list"][weather_data_total - 1]["weather"][0]["main"]
            wind_speed = response.json()["list"][weather_data_total - 1]["wind"]["speed"]
        
        for data_point in data:
            convert = datetime.fromtimestamp(dt).strftime("%A, %B %d, %Y %I:%M:%S")
            print(convert)

if __name__ == "__main__":
    weather = Weather()
    weather.get_data(weather_key, city, state)
