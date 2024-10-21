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

print(gasLevelGauge())
print(gasStation())