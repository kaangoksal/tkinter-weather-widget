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

        basic_temp_label = tk.Label(self,text="Temperature: ")
        basic_temp_label.grid(column=1, row=0)

        self.temp_value_label = tk.Label(self,text=" ? ")
        self.temp_value_label.grid(column=1,row=0)

        table_frame = tk.Frame(self)
        table_frame.grid(column=0,row=0)

        image1 = WeatherWidget.create_image_label(self, "./images/wind.png")
        image2 = WeatherWidget.create_image_label(self, "./images/cloudy.png")
        image3 = WeatherWidget.create_image_label(self, "./images/visibility.png")
        image4 = WeatherWidget.create_image_label(self, "./images/sattalite.png")
        image5 = WeatherWidget.create_image_label(self, "./images/temperature.png")
        image6 = WeatherWidget.create_image_label(self, "./images/rain.png")

        image1.grid(column=1,row=0)
        image6.grid(column=2,row=0)
        image5.grid(column=3,row=0)
        image4.grid(column=4,row=0)
        image3.grid(column=5,row=0)
        image2.grid(column=6,row=0)





    @staticmethod
    def create_image_label(parent,image_path):
        _image = Image.open(image_path)
        _image = _image.resize((32, 32), Image.ANTIALIAS)
        _image = ImageTk.PhotoImage(_image)

        globe_image_label = tk.Label(parent, image=_image)
        globe_image_label.image = _image
        return globe_image_label
