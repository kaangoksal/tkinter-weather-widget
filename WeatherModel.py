from datetime import datetime
from LocationModel import LocationModel

class WeatherModel:

    def __init__(self, location:LocationModel, date: datetime,
                 rain: int,
                 temperature: int,
                 max_temperature: int,
                 min_temperature: int,
                 humidity: int,
                 wind: int,
                 cloud_percentage:int,
                 pressure:int,
                 sat_count: int,
                 visibility:int,wind_degree=999):

        self.location = location
        self.wind_speed = wind
        self.rain_chance = rain
        self.temperature = temperature
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.date = date
        self.humidity = humidity
        self.visibility = visibility
        self.sat_count = sat_count
        self.cloud_percentage = cloud_percentage
        self.pressure = pressure
        self.wind_degree = wind_degree

    def get_hour_minute(self):

        return str(self.date.hour)+":"+str(self.date.minute)