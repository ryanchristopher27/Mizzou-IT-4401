# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Paint Job Estimator
# Module 4

# Imports
import math

# References
    # 1) https://www.reddit.com/r/learnpython/comments/45c9kw/adding_or_in_python_without_space_in_between_the/

# Functions
def doCalculation(area, cost):
    gallonCoverage = 350
    labor = float(62.25)
    hoursPerGallon = 6

    gallonsNeeded = area/gallonCoverage
    laborHours = float(gallonsNeeded*hoursPerGallon)
    laborCost = float(laborHours*labor)
    paintCost = float(math.ceil(gallonsNeeded)*cost)
    totalCost = float(laborCost + paintCost)

    # Display Calculations
    print("\n")
    print("Gallons of Paint: ", math.ceil(gallonsNeeded))
    print("Hours of Labor:   ", '{:.1f}'.format(laborHours)) # Code from Reference 1
    print("Cost of Paint:    ", '${:.2f}'.format(paintCost)) # Code from Reference 1
    print("Cost of Labor:    ", '${:.2f}'.format(laborCost)) # Code from Reference 1
    print("Total Cost:       ", '${:.2f}'.format(totalCost)) # Code from Reference 1
    print("\n")

# Main Code
print("Welcome to the Paint Job Estimator")

repeat = True
while (repeat):
    print("Please enter the required information below\n")

    # Gets square feet of wall from user
    sqftHold = True
    while (sqftHold):
        try:
            squareFeet = float(input("\nSquare Feet of Wall Space to be Painted: "))
            if (squareFeet <= 0):
                print("Value must be positive.")
                continue
        except ValueError:
            print("The value you entered is invalid. Please enter a numerical value.")
        else:
            sqftHold = False

    # Gets Cost of Paint per Gallon
    ppgHold = True
    while (ppgHold):
        try:
            paintPerGallon = float(input("Cost of Paint Per Gallon: "))
            if (paintPerGallon <= 0):
                print("Value must be positive.")
                continue
        except ValueError:
            print("The value you entered is invalid. Please enter a numerical value.")
        else:
            ppgHold = False

    # Call doCalculation Function
    doCalculation(squareFeet, paintPerGallon)

    # Checks if another calculation should be performed
    repeatVal = input("Would you like to perform another calculation? (y/n)\t")
    if (repeatVal == "y"):
        repeat = True
    else:
        repeat = False

print("Thank you for using the Paint Job Estimator!")