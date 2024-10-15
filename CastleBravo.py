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
    weather_forecast = ["Snowy", "Blizzard", "Rainy", "Windy", "Icy", "Sunny"]
    # Randomly select one weather condition from the list
    weather_condition = random.choice(weather_forecast)
    return weather_condition

# Store the selected weather condition in the variable 'weather_alert'
weather_alert = weather()

# Function to handle the vehicle's response to the weather condition
def vehicle_response_system(weather_alert):
    # Dictionary to map weather conditions to their respective alarm delays and speed limits
    weather_responses = {
        "Snowy": {"delay": 30, "speed_limit": 55},
        "Blizzard": {"delay": 45, "speed_limit": 45},
        "Rainy": {"delay": 15, "speed_limit": 65},
        "Windy": {"delay": 5, "speed_limit": 70},
        "Icy": {"delay": 50, "speed_limit": 30}
    }

    # Check if the weather condition is in the dictionary
    if weather_alert in weather_responses:
        response = weather_responses[weather_alert]
        print(f"\nThe National Weather Service Updated Our Alarm By {response['delay']} Minutes Because "
              f"Of The Forecast Of {weather_alert} Weather Condition.")
        sleep(1)  # Add a short delay before printing the next line
        print(f"\nVRS System Has Been Engaged Only Allowing To Drive {response['speed_limit']}MPH")
    else:
        # For any weather condition not specified above, assume the weather is clear (Sunny)
        print(f"The National Weather Service Is Calling For {weather_alert} Skies")
        sleep(1)
        print("VRS Has Been Disabled")

# Call the vehicle response system function to execute the weather-based logic
vehicle_response_system(weather_alert)
