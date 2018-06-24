
from WeatherWidget import WeatherWidget
from WeatherWidgetAPI import WeatherWidgetAPI
from WeatherModel import WeatherModel

class WeatherWidgetController():

    def __init__(self,widget_view:WeatherWidget,weather_api:WeatherWidgetAPI, current_location):
        self.weather_api = weather_api
        self.widget_view = widget_view

        self.current_location = current_location #TODO maybe a location object?

    def get_data_from_api_and_pump_it_to_view(self):

        weather_data = self.weather_api.get_current_weather_at_coorindates(self.current_location.latitude,self.current_location.longitude)
        satalite_data = self.weather_api.get_satellite_visibility(self.current_location.latitude,self.current_location.longitude)

        # todo combine the weather and satalite data to create weather objects and pass them to view


        self.widget_view.populate_data(weather_data_list)
