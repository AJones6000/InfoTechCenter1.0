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
    elif WeatherAlert == "Rainy":
        print("\nThe National Weather Service Updated Our Alarm By 15 Minutes Because "
              "Of The Forcast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 65MPH")
    elif WeatherAlert == "Windy":
        print("\nThe National Weather Service Updated Our Alarm By 5 Minutes Because "
              "Of The Forcast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 70MPH")
    elif WeatherAlert == "Icy":
        print("\nThe National Weather Service Updated Our Alarm By 50 Minutes Because "
              "Of The Forcast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 30MPH")
    else:
        print("The National Weather Service Is Calling For",WeatherAlert," Skies")
        sleep(1)
        print("VRS Has Been Disabled")




vehicaleResponseSysterm()