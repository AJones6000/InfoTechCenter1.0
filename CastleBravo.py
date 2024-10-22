print("\n***************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGauge():
    GasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    return random.choice(GasLevelList)

def gasStation():
    gasStationList=["VP","Shell","Sams Club","Marathon","Mobile","Speedway","Circle K"]
    return random.choice(gasStationList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("WARNING YOU ARE ON EMPTY")
        sleep(3)
        print("\n calling AAA")
    elif gasLevelIndicator == "Low":
        print("Your Gas Tank Is Very Low, Checking GPS For Gas Station")
        sleep(2)
        print("The Closest Gas Station Is",gasStation(),"Which Is",milesToGasStationLow,"Mile Away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your Gas Tank Is A Quarter Tank, Checking GPS For Gas Station")
        sleep(2)
        print("The Closest Gas Station Is",gasStation(),"Which Is",milesToGasStationQuarterTank,"Mile Away")
    elif gasLevelIndicator == "Half Tank":
        print("Your Gas Tank Is Half Full")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You Gas Tank Is Three Quarters Full")
    else: print("You Have A Full Tank")
gasLevelAlert()