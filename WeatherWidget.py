import tkinter as tk  # python 3
from tkinter import *
from PIL import ImageTk, Image


class WeatherWidget(tk.LabelFrame):
    """
    Each of these frames represent a view
    """

    def __init__(self, parent):

        tk.LabelFrame.__init__(self, parent)
        self.configure(text="Weather")

        self.data_grid_size = 5
        self.data_elements = []

        # basic_temp_label = tk.Label(self,text="Temperature: ")
        # basic_temp_label.grid(column=1, row=0)
        #
        # self.temp_value_label = tk.Label(self,text=" ? ")
        # self.temp_value_label.grid(column=1,row=0)

        self.table_frame = tk.Frame(self)
        self.table_frame.grid(column=0,row=0)



        wind_image = WeatherWidget.create_image_label(self.table_frame, "./images/wind.png")
        cloud_image = WeatherWidget.create_image_label(self.table_frame, "./images/cloudy.png")
        visibility_image = WeatherWidget.create_image_label(self.table_frame, "./images/visibility.png")
        satallite_image = WeatherWidget.create_image_label(self.table_frame, "./images/sattalite.png")
        temperature_image = WeatherWidget.create_image_label(self.table_frame, "./images/temperature.png")
        rain_image = WeatherWidget.create_image_label(self.table_frame, "./images/rain.png")
        time_image = WeatherWidget.create_image_label(self.table_frame, "./images/time.png")

        time_image.grid(column=0,row=0)
        wind_image.grid(column=1,row=0)
        rain_image.grid(column=2,row=0)
        temperature_image.grid(column=3,row=0)
        satallite_image.grid(column=4,row=0)
        visibility_image.grid(column=5,row=0)
        cloud_image.grid(column=6,row=0)

        self.initialize_data_grid()


    def initialize_data_grid(self):

        for i in range(1,self.data_grid_size+1):
            new_row =[]

            for j in range(7):
                data_label = tk.Label(self.table_frame,text="?")
                data_label.grid(column=j,row=i)
                new_row.append(data_label)

            self.data_elements.append(new_row)


    def populate_data(self, weather_data_list:list):

        # TODO sort the data according to time

        for i in range(self.data_grid_size):
            weather_data = weather_data_list[i]
            row_label_list = self.data_elements[i]

            time = weather_data.get_hour_minute()
            wind = weather_data.wind
            rain_chance = weather_data.rain_chance
            temperature = weather_data.temperature
            humidity = weather_data.humidity
            visibility = weather_data.visibility
            sat_count = weather_data.sat_count
            cloud_percentage = weather_data.cloud_percentage

            row_label_list[0].configure(text=time)
            row_label_list[1].configure(text=str(wind))
            row_label_list[2].configure(text=str(rain_chance))
            row_label_list[3].configure(text=str(temperature))
            row_label_list[4].configure(text=str(sat_count))
            row_label_list[5].configure(text=str(visibility))
            row_label_list[6].configure(text=str(cloud_percentage))



    @staticmethod
    def create_image_label(parent,image_path):
        _image = Image.open(image_path)
        _image = _image.resize((32, 32), Image.ANTIALIAS)
        _image = ImageTk.PhotoImage(_image)

        globe_image_label = tk.Label(parent, image=_image)
        globe_image_label.image = _image
        return globe_image_label
