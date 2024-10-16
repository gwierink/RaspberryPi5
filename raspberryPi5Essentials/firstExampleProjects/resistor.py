#==============================================================================
#
#                               Resistor color codes
#                               --------------------
#
# The user enters the three colours of a resistor and the program calculates
# and displays the value of the resistor in Ohms.
#
# Program: resistor.py
# Date:    16/10/2024
# Author:  Dogan Ibrahim
#==============================================================================

colours = ['black','brown','red','orange','yellow','green','blue','violet',\
           'grey','white']

print("Resistor value calculator")
print("=========================")
yn = "y"

while yn == 'y':
    FirstColour  = input("Enter first colour: ")
    SecondColour = input("Enter second colour: ")
    ThirdColour  = input("Enter third colour: ")

# Convert to lower case
    FirstColour  = FirstColour.lower()
    SecondColour = SecondColour.lower()
    ThirdColour  = ThirdColour.lower()

# Find the values of colours
    FirstValue  = colours.index(FirstColour)
    SecondValue = colours.index(SecondColour)
    ThirdValue  = colours.index(ThirdColour)

# Calculate the value of the resistor
    Resistor = 10 * FirstValue + SecondValue
    Resistor = Resistor * (10 ** ThirdValue)
    print("Resistance = %d Ohms" % (Resistor))

# Ask for more
    yn = input("\nDo you want to continue?: ")
    yn = yn.lower()
