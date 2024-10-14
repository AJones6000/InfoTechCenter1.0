print("\n*******************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["Snowing", "Blizzard", "Rainy","Windy","Icy","Sunny"]
    WeatherCondition = random.choice(weatherForecast)
    return WeatherCondition

print(weather())