
from tkinter import Tk, Label, Button
import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from WeatherWidget import WeatherWidget

class MyFirstGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.label = Label(self, text="This is our first GUI!")
        self.label.grid(column=1,row=1)

        self.greet_button = Button(self, text="Greet", command=self.greet)
        self.greet_button.grid(column=1,row=2)

        self.close_button = Button(self, text="Close", command=self.quit)
        self.close_button.grid(column=1,row=3)

        self.weather_widget = WeatherWidget(self)
        self.weather_widget.grid(column=1, row=4, pady=(10,10),padx=(10,10))

    def greet(self):
        print("Greetings!")


my_gui = MyFirstGUI()
my_gui.mainloop()