from datetime import datetime


class WeatherModel:

    def __init__(self, date: datetime, rain: int, temperature: int, humidity: int, wind: int):
        self.wind = wind
        self.rain = rain
        self.temperature = temperature
        self.date = date
        self.humidity = humidity
