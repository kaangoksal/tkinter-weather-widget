from datetime import datetime


class WeatherModel:

    def __init__(self, date: datetime,
                 rain: int,
                 temperature: int,
                 humidity: int,
                 wind: int,
                 cloud_percentage:int,
                 sat_count: int,
                 visibility:int ):

        self.wind_speed = wind
        self.rain_chance = rain
        self.temperature = temperature
        self.date = date
        self.humidity = humidity
        self.visibility = visibility
        self.sat_count = sat_count
        self.cloud_percentage = cloud_percentage

    def get_hour_minute(self):

        return str(self.date.hour)+":"+str(self.date.minute)