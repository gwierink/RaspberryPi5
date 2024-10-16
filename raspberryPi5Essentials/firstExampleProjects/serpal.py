#==============================================================================
#
#                               Resistor color codes
#                               --------------------
#
# This program calculates the total resistance of serial or parallel
# connected resistors.
#
# Program: serpal.py
# Date:    16/10/2024
# Author:  Dogan Ibrahim
#==============================================================================

print("Resistors in series or parallel")
print("===============================")
yn = "y"

while yn == 'y':
    N = int(input("\nHow many resistors are there?: "))
    mode = input("Are the resistors series (s) or parallel (p)?: ")
    mode = mode.lower()

# Read the resistor values and calculate the total
    resistor = 0.0

    if mode == 's':
        for n in range(0,N):
            s = "Enter resistor " + str(n+1) + " value in Ohhms: "
            r = int(input(s))
            resistor = resistor + r
        print("Total resistace = %d Ohms" %(resistor))

    elif mode == 'p':
        for n in range(0,N):
            s = "Enter resistor " + str(n+1) + " value in Ohhms: "
            r = float(input(s))
            resistor = resistor + 1 / r
        print("Total resistace = %.2f Ohms" %(1 / resistor))

# Check if the user wants to exit
    yn = input("\nDo you want to continue?: ")
    yn = yn.lower()
