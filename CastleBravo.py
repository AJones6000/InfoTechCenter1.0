print("\n***************************\n")  # Print a separator for better readability in the output

print("Gasoline Branch")  # Print the section title

import random  # Import the random module to randomly choose values for gas level and gas station
from time import sleep  # Import sleep from the time module to introduce pauses in the output


# Function to simulate the current gas level
def gasLevelGauge():
    GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly choose a gas level from the list
    return random.choice(GasLevelList)


# Function to simulate a random gas station
def gasStation():
    gasStationList = ["VP", "Shell", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly choose a gas station from the list
    return random.choice(gasStationList)


# Function to alert the driver based on the current gas level
def gasLevelAlert():
    # Generate a random distance between 1 and 25 miles for a "Low" gas level
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    # Generate a random distance between 25.1 and 50 miles for a "Quarter Tank" gas level
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)

    # Get the current gas level using the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Check the gas level and print the appropriate message
    if gasLevelIndicator == "Empty":
        print("WARNING YOU ARE ON EMPTY")  # Critical alert for an empty tank
        sleep(3)  # Pause for 3 seconds before the next message
        print("\n calling AAA")  # Simulate calling for roadside assistance

    elif gasLevelIndicator == "Low":
        print("Your Gas Tank Is Very Low, Checking GPS For Gas Station")  # Alert for a low gas level
        sleep(2)  # Pause for 2 seconds
        print("The Closest Gas Station Is", gasStation(), "Which Is", milesToGasStationLow,
              "Mile Away")  # Show nearest gas station

    elif gasLevelIndicator == "Quarter Tank":
        print("Your Gas Tank Is A Quarter Tank, Checking GPS For Gas Station")  # Alert for a quarter tank level
        sleep(2)  # Pause for 2 seconds
        print("The Closest Gas Station Is", gasStation(), "Which Is", milesToGasStationQuarterTank,
              "Mile Away")  # Show nearest gas station

    elif gasLevelIndicator == "Half Tank":
        print("Your Gas Tank Is Half Full")  # Inform the user that the gas level is half full

    elif gasLevelIndicator == "Three Quarter Tank":
        print("You Gas Tank Is Three Quarters Full")  # Inform the user that the gas level is three-quarters full

    else:
        print("You Have A Full Tank")  # Inform the user that the gas tank is full


# Call the gasLevelAlert function to run the alert system
gasLevelAlert()
