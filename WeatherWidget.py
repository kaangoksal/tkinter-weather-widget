
import tkinter as tk  # python 3
from tkinter import *

class WeatherWidget(tk.LabelFrame):
    """
    Each of these frames represent a view
    """

    def __init__(self, parent):

        tk.LabelFrame.__init__(self, parent)
        self.configure(text="Weather")

        basic_temp_label = tk.Label(self,text="Temperature: ")
        basic_temp_label.grid(column=0, row=0)

        self.temp_value_label = tk.Label(self,text=" ? ")
        self.temp_value_label.grid(column=1,row=0)
