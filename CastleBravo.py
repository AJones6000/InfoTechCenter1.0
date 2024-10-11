import sys  # Import the sys module for system-specific parameters and functions
import time  # Import the time module for time-related functions

# Print a welcome message to the user
print("\n\tWelcome to InfoTechCenter\n")
TimeToSleep=1 #variable to set the time library to 1 seconds
time.sleep(TimeToSleep)#calling the TimeToSleep variable
# Initialize variables
x = 0  # Counter for booting iterations
ellipsis = 0  # Counter for the ellipsis (dots) in the booting message

# Loop until the counter reaches 20 (simulating a boot process)
while x != 20:
    x += 1  # Increment the boot iteration counter
    # Create the booting message with a dynamic number of dots
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment the ellipsis counter
    sys.stdout.write("\r" + message)  # Write the message to the console, overwriting the previous line
    time.sleep(0.5)  # Pause for half a second to simulate booting delay

    # Reset the ellipsis counter after it reaches 4
    if ellipsis == 4:
        ellipsis = 0

    # When the counter reaches 20, print the final message
    if x == 20:
        print("\n\nOperating System Booted Up")
