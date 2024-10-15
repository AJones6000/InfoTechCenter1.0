print("\n*******************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["Snowy", "Blizzard", "Rainy","Windy","Icy","Sunny"]
    WeatherCondition = random.choice(weatherForecast)
    return WeatherCondition

WeatherAlert = weather()

def vehicaleResponseSysterm():
    if WeatherAlert == "Snowy":
        print("\nThe National Weather Service Updated Our Alarm By 30 Minutes Because "
              "Of The Forcast Of",WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 55MPH")
    elif WeatherAlert == "Blizzard":
        print("\nThe National Weather Service Updated Our Alarm By 45 Minutes Because "
              "Of The Forcast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 45MPH")



vehicaleResponseSysterm()