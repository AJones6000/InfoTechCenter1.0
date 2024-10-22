import random  # Import random to randomly select values for gas level and gas stations
from time import sleep  # Import sleep to introduce delays for a more realistic simulation


# Function to simulate the current gas level
def gasLevelGauge():
    # List of possible gas levels in the tank
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


# Function to simulate finding a nearby gas station
def gasStation():
    # List of gas station brands
    return random.choice(["VP", "Shell", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"])


# Function to handle pluralization of miles
def formatMiles(miles):
    return f"{miles} mile{'s' if miles != 1 else ''}"


# Function to handle searching for the closest gas station and printing the message
def findNearestGasStation(miles):
    station = gasStation()  # Find a random nearby gas station
    print(f"The closest gas station is {station}, which is {formatMiles(miles)} away.")


# Function to provide a gas level alert based on the current tank level
def gasLevelAlert():
    # Define random distances to the nearest gas station
    miles_to_station_low = round(random.uniform(1, 25), 1)  # For "Low" level
    miles_to_station_quarter = round(random.uniform(25.1, 50), 1)  # For "Quarter Tank"

    # Get the current gas level
    gas_level = gasLevelGauge()

    # Handling based on gas level
    if gas_level == "Empty":
        print("WARNING: Your tank is EMPTY!")  # Critical warning
        sleep(3)  # Pause for urgency
        print("\nCalling AAA for roadside assistance...")  # Simulate calling AAA

    elif gas_level == "Low":
        print("Your gas tank is very low! Searching for nearby gas stations...")
        sleep(2)
        findNearestGasStation(miles_to_station_low)  # Reuse the generic gas station search logic

    elif gas_level == "Quarter Tank":
        print("Your gas tank is at a quarter. Searching for nearby gas stations...")
        sleep(2)
        findNearestGasStation(miles_to_station_quarter)  # Reuse the generic gas station search logic

    elif gas_level == "Half Tank":
        print("Your gas tank is half full.")  # Inform the user

    elif gas_level == "Three Quarter Tank":
        print("Your gas tank is three-quarters full.")  # Inform the user

    else:
        print("Your tank is full. You're good to go!")  # Full tank message


# Call the gasLevelAlert function to initiate the gas level check
gasLevelAlert()
