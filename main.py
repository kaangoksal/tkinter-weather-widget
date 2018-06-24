
from tkinter import Tk, Label, Button
import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from WeatherWidget import WeatherWidget

class MyFirstGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.label = Label(self, text="Weather widget sample ")
        self.label.grid(column=1,row=1)


        self.weather_widget = WeatherWidget(self)
        self.weather_widget.grid(column=1, row=4, pady=(10,10),padx=(10,10))

        # TODO Intialize weather widget controller and apis


my_gui = MyFirstGUI()
my_gui.mainloop()