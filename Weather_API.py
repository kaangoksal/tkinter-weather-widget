from datetime import datetime
import json
import urllib.request
import tkinter
from tkinter import Tk, PhotoImage
import sys
import os
from WeatherModel import WeatherModel
from LocationModel import LocationModel
#
class WeatherAPI:
    
    def __init__(self):
        #TODO add key to the constructor so we don't get our api key stolen, use it as self.api_key, take a look at
        # OpenWeatherAPI.py, this one will replace that
        pass

    def time_converter(self, time):
        converted_time = datetime.fromtimestamp(
            int(time)
        ).strftime('%I:%M %p')
        return converted_time

    def url_builderCurrent(self, lat, long):
        user_api = 'WE DONT UPLOAD KEYS TO GITHUB :)'
        unit = 'metric'
        api = 'http://api.openweathermap.org/data/2.5/weather?'
        full_api_url = api + 'lat=' + str(lat) + '&' + 'lon=' + str(long) + '&mode=json&units=' + unit + '&appid=' + user_api
        return full_api_url

    def url_builderForecast(self, lat, long):
        user_api = 'WE DONT UPLOAD KEYS TO GITHUB :)'
        unit = 'metric'
        api = 'http://api.openweathermap.org/data/2.5/forecast?'
        full_api_url = api + 'lat=' + str(lat) + '&' + 'lon=' + str(long) + '&mode=json&units=' + unit + '&appid=' + user_api
        return full_api_url

    def data_fetch(self, full_api_url):
        url = urllib.request.urlopen(full_api_url)
        output = url.read().decode('utf-8')
        raw_api_dict = json.loads(output)
        url.close()
        return raw_api_dict

    def data_organizerForecast(self, raw_api_dict):

        city_dict = raw_api_dict["city"]
        coordinates = city_dict["coord"]

        location_of_the_forecast = LocationModel(coordinates["lat"], coordinates["lon"])

        total_elements = raw_api_dict["cnt"]

        element_list = raw_api_dict["list"]

        data = []
        for element in element_list:

            date_string = element["dt_txt"]

            # '2018-07-01 09:00:00'
            #datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

            wind_dict = element["wind"]

            wind_speed = wind_dict["speed"]
            wind_degree = wind_dict["deg"]

            rain_dict = element["rain"]

            rain_chance = rain_dict.get("3h", 0)

            weather_dict = element["weather"][0]

            weather_description = weather_dict["description"]
            # I believe we don't need much from here...

            main_dict = element["main"]

            pressure = main_dict['pressure']
            ground_level = main_dict['grnd_level']
            sea_level = main_dict['sea_level']

            temp_kf = main_dict['temp_kf']
            temp_max = main_dict["temp_max"]
            temp_min = main_dict['temp_min']
            temp = main_dict['temp']

            humidity = main_dict['humidity']

            cloud_dict = element["clouds"]

            cloud_coverage = cloud_dict["all"]




            # temp = raw_api_dict['list'][elements]['main'].get('temp'),
            # temp_max = raw_api_dict['list'][elements]['main'].get('temp_max'),
            # temp_min = raw_api_dict['list'][elements]['main'].get('temp_min'),
            # humidity = raw_api_dict['list'][elements]['main'].get('humidity'),
            # pressure = raw_api_dict['list'][elements]['main'].get('pressure'),
            # sky = raw_api_dict['list'][elements]['weather'][0]['main'],
            # wind = raw_api_dict['list'][elements]['wind'].get('speed'),
            # wind_deg = raw_api_dict['list'][elements]['wind'].get('deg'),
            # dt_txt = raw_api_dict['list'][elements]['dt_txt'],
            # cloudiness=raw_api_dict['list'][elements]['clouds'].get('all'),
            # rain=raw_api_dict['list'][elements]['rain'],
            # typeid=raw_api_dict['list'][elements]['weather'][0]['id'],
            # wtype=raw_api_dict['list'][elements]['weather'][0]['description']
            
            sat_count = 0
            visibility = 0
            #TODO fill date time as well
            #TODO integrate sat count as well
            new_weather_model = WeatherModel(location_of_the_forecast, date,
                                             rain_chance,
                                             temp,
                                             temp_max,
                                             temp_min,
                                             humidity,
                                             wind_speed,
                                             cloud_coverage,
                                             sat_count,
                                             visibility,
                                             pressure, wind_degree=wind_degree)
            data.append(new_weather_model)
        # These can be placed inside the weather model, but as a coordinate, we are mostly interested in weather
        # conditions at spesific coords, (wont fly drones over a city wide area)
        # data['city'] = raw_api_dict.get('city').get('name')
        # data['country'] = raw_api_dict.get('city').get('country'),

        return data

    def data_organizer(self, raw_api_dict):
        data = dict(
            city=raw_api_dict.get('name'),
            country=raw_api_dict.get('sys').get('country'),
            temp=raw_api_dict.get('main').get('temp'),
            temp_max=raw_api_dict.get('main').get('temp_max'),
            temp_min=raw_api_dict.get('main').get('temp_min'),
            humidity=raw_api_dict.get('main').get('humidity'),
            pressure=raw_api_dict.get('main').get('pressure'),
            sky=raw_api_dict['weather'][0]['main'],
            sunrise=self.time_converter(raw_api_dict.get('sys').get('sunrise')),
            sunset=self.time_converter(raw_api_dict.get('sys').get('sunset')),
            wind=raw_api_dict.get('wind').get('speed'),
            wind_deg=raw_api_dict.get('deg'),
            dt=self.time_converter(raw_api_dict.get('dt')),
            cloudiness=raw_api_dict.get('clouds').get('all'),
            typeid = raw_api_dict['weather'][0]['id'],
            wtype=raw_api_dict['weather'][0]['description']
        )
        return data



    def get_current_weather_at_coordinates(self, latitude, longitude):
        return self.data_organizer(self.data_fetch(self.url_builderCurrent(latitude, longitude)))


    def get_weather_prediction_at_coordinates(self, latitude, longitude):
        return self.data_organizerForecast(self.data_fetch(self.url_builderForecast(latitude, longitude)))

    def get_satellite_visibility(self, latitude, longitude):
        pass


myAPI = WeatherAPI()
print(myAPI.get_weather_prediction_at_coordinates(48.137154, 11.576124))