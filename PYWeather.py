#Python 3X

import PIL.ImageTk
import PIL.Image 
from tkinter import *
import tkinter as tk

#Window Size and Title Setting

window = tk.Tk()
window.title("PyWeather")
window.geometry("580x275")

WeatherLabelFrame = LabelFrame(window, text = "  Weather Status  ", padx = 10, pady = 10)
#padx: frame width size #pady: frame height size

WeatherLabelFrame.grid(row = 0, column = 0, padx = 10, pady = 10)
#padx: window and labelFrame margin(X-Width) #pady: window and labelFrame margin(Y-Height)

#Picture Path and Size Setting

Time = PIL.Image.open("images/time.png")
Time = Time.resize((32, 32), PIL.Image.ANTIALIAS)
Time = PIL.ImageTk.PhotoImage(Time)

Cloud = PIL.Image.open("images/cloud.png")
Cloud = Cloud.resize((32, 32), PIL.Image.ANTIALIAS)
Cloud = PIL.ImageTk.PhotoImage(Cloud)

Rain = PIL.Image.open("images/rain.png")
Rain = Rain.resize((32, 32), PIL.Image.ANTIALIAS)
Rain = PIL.ImageTk.PhotoImage(Rain)

Sattalite = PIL.Image.open("images/sattalite.png")
Sattalite = Sattalite.resize((32, 32), PIL.Image.ANTIALIAS)
Sattalite = PIL.ImageTk.PhotoImage(Sattalite)

Temperature = PIL.Image.open("images/temperature.png")
Temperature = Temperature.resize((32, 32), PIL.Image.ANTIALIAS)
Temperature = PIL.ImageTk.PhotoImage(Temperature)

Visibility = PIL.Image.open("images/visibility.png")
Visibility = Visibility.resize((32, 32), PIL.Image.ANTIALIAS)
Visibility = PIL.ImageTk.PhotoImage(Visibility)

Wind = PIL.Image.open("images/wind.png")
Wind = Wind.resize((32, 32), PIL.Image.ANTIALIAS)
Wind = PIL.ImageTk.PhotoImage(Wind)

#Picture Align Setting

TimeLabel = Label(WeatherLabelFrame, image = Time)
CloudLabel = Label(WeatherLabelFrame, image = Cloud)
RainLabel = Label(WeatherLabelFrame, image = Rain)
SattaliteLabel = Label(WeatherLabelFrame, image = Sattalite)
TemperatureLabel = Label(WeatherLabelFrame, image = Temperature)
VisibilityLabel = Label(WeatherLabelFrame, image = Visibility)
WindLabel = Label(WeatherLabelFrame, image = Wind)

TimeLabel.grid(row = 0, column = 0)
CloudLabel.grid(row = 0, column = 6)
RainLabel.grid(row = 0, column = 2)
SattaliteLabel.grid(row = 0, column = 4)
TemperatureLabel.grid(row = 0, column = 3)
VisibilityLabel.grid(row = 0, column = 5)
WindLabel.grid(row = 0, column = 1)

#Weather Data Align Setting

FirstRowTimeLabel = Label(WeatherLabelFrame, text = "15:00")
SecondRowTimeLabel = Label(WeatherLabelFrame , text = "16:00")
ThirdRowTimeLabel = Label(WeatherLabelFrame , text = "17:00")

FirstWindLabel = Label(WeatherLabelFrame, text = "85" + "km/h")
SecondWindLabel = Label(WeatherLabelFrame, text = "39" + "km/h")
ThirdWindLabel = Label(WeatherLabelFrame, text = "56" + "km/h")

FirstRainLabel = Label(WeatherLabelFrame, text = "%" + "90")
SecondRainLabel = Label(WeatherLabelFrame, text = "%" + "70")
ThirdRainLabel = Label(WeatherLabelFrame, text = "%" + "87")

FirstSattaliteLabel = Label(WeatherLabelFrame, text = "55")
SecondSattaliteLabel = Label(WeatherLabelFrame, text = "20")
ThirdSattaliteLabel = Label(WeatherLabelFrame, text = "90")

FirstTemperatureLabel = Label(WeatherLabelFrame, text = "27" + "°C")
SecondTemperatureLabel = Label(WeatherLabelFrame, text = "55" + "°C")
ThirdTemperatureLabel = Label(WeatherLabelFrame, text = "55" + "°C")

FirstVisibilityLabel = Label(WeatherLabelFrame, text = "28")
SecondVisibilityLabel = Label(WeatherLabelFrame, text = "45")
ThirdVisibilityLabel = Label(WeatherLabelFrame, text = "18")

FirstCloudLabel = Label(WeatherLabelFrame, text = "%" + "12")
SecondCloudLabel = Label(WeatherLabelFrame, text = "%" + "29")
ThirdCloudLabel = Label(WeatherLabelFrame, text = "%" + "49")


FirstRowTimeLabel.grid(row = 1, column = 0)
SecondRowTimeLabel.grid(row = 2, column = 0)
ThirdRowTimeLabel.grid(row = 3, column = 0)

FirstWindLabel.grid(row = 1, column = 1)
SecondWindLabel.grid(row = 2, column = 1)
ThirdWindLabel.grid(row = 3, column = 1)

FirstRainLabel.grid(row = 1, column = 2)
SecondRainLabel.grid(row = 2, column = 2)
ThirdRainLabel.grid(row = 3, column = 2)

FirstTemperatureLabel.grid(row = 1, column = 3)
SecondTemperatureLabel.grid(row = 2, column = 3)
ThirdTemperatureLabel.grid(row = 3, column = 3)

FirstSattaliteLabel.grid(row = 1, column = 4)
SecondSattaliteLabel.grid(row = 2, column = 4)
ThirdSattaliteLabel.grid(row = 3, column = 4)

FirstVisibilityLabel.grid(row = 1, column = 5)
SecondVisibilityLabel.grid(row = 2, column = 5)
ThirdVisibilityLabel.grid(row = 3, column = 5)

FirstCloudLabel.grid(row = 1, column = 6)
SecondCloudLabel.grid(row = 2, column = 6)
ThirdCloudLabel.grid(row = 3, column = 6)


#Country / City & Location Setting

CountryLabel = Label(WeatherLabelFrame, text = "İstanbul")
NorthLabel = Label(WeatherLabelFrame, text = "North: " + "34.324158")
EastLabel = Label(WeatherLabelFrame, text = "East: " + "41.324158")
DataHistoryLabel = Label(WeatherLabelFrame, text = "Last Data: " + "15" + "mins ago") 

CountryLabel.grid(row = 0, column = 7)
NorthLabel.grid(row = 1, column = 7)
EastLabel.grid(row = 2, column = 7)
DataHistoryLabel.grid(row = 3, column =7)

window.mainloop()
















