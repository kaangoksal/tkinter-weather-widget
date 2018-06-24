import requests


class WeatherWidgetAPI:

    def __init__(self, sattalite_api, weather_api):
        self.satallite_api = sattalite_api
        self.weather_api = weather_api

    def get_current_weather_at_coorindates(self, latitude, longitude):
        return self.weather_api.get_current_weather_by_coordinates(latitude, longitude)


    def get_weather_prediction_at_coordinates(self, latitude, longitude):
        return self.weather_api.get_weather_predictions_by_coordinate(latitude,longitude)

    def get_satellite_visibility(self, latitude, longitude):
        return self.satallite_api.get_sattalite_visibility_data_on_coordinates(latitude,longitude)
