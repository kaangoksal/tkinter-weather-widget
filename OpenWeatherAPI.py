import requests


class OpenWeatherAPI:

    def __init__(self, key):
        self.key = key


    def get_current_weather_by_coordinates(self, latitude,longitude):

        url = "http://api.openweathermap.org/data/2.5/weather"

        querystring = {"lat": latitude, "lon": longitude, "units": "metric",
                       "APPID": self.key}

        response = requests.request("GET", url, params=querystring)

        #TODO error handling, such as invalid key
        return response.json()


