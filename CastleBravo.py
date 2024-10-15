# Print a divider line to make the output clearer
print("\n*******************************************\n")

# Print the title for the weather branch section
print("Weather Branch\n")

# Import necessary libraries
import random  # Used to randomly select a weather condition
from time import sleep  # Used to add delays in the output for a more realistic effect

# Function to determine the weather condition
def weather():
    # List of possible weather conditions
    weatherForecast = ["Snowy", "Blizzard", "Rainy", "Windy", "Icy", "Sunny"]
    # Randomly select one weather condition from the list
    WeatherCondition = random.choice(weatherForecast)
    return WeatherCondition

# Store the selected weather condition in the variable 'WeatherAlert'
WeatherAlert = weather()

# Function to handle the vehicle's response to the weather condition
def vehicaleResponseSysterm():  # Note: Correct spelling would be "vehicleResponseSystem"
    # Check the weather condition and print appropriate responses
    if WeatherAlert == "Snowy":
        print("\nThe National Weather Service Updated Our Alarm By 30 Minutes Because "
              "Of The Forecast Of", WeatherAlert, "Weather Condition.")
        sleep(1)  # Add a short delay before printing the next line
        print("\nVRS System Has Been Engaged Only Allowing To Drive 55MPH")
    elif WeatherAlert == "Blizzard":
        print("\nThe National Weather Service Updated Our Alarm By 45 Minutes Because "
              "Of The Forecast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 45MPH")
    elif WeatherAlert == "Rainy":
        print("\nThe National Weather Service Updated Our Alarm By 15 Minutes Because "
              "Of The Forecast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 65MPH")
    elif WeatherAlert == "Windy":
        print("\nThe National Weather Service Updated Our Alarm By 5 Minutes Because "
              "Of The Forecast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 70MPH")
    elif WeatherAlert == "Icy":
        print("\nThe National Weather Service Updated Our Alarm By 50 Minutes Because "
              "Of The Forecast Of", WeatherAlert, "Weather Condition.")
        sleep(1)
        print("\nVRS System Has Been Engaged Only Allowing To Drive 30MPH")
    else:
        # For any weather condition not specified above, assume the weather is clear (Sunny)
        print("The National Weather Service Is Calling For", WeatherAlert, "Skies")
        sleep(1)
        print("VRS Has Been Disabled")

# Call the vehicle response system function to execute the weather-based logic
vehicaleResponseSysterm()
