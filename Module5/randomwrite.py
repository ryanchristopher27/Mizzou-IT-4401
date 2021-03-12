# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Random Write
# Module 5

# Imports
import math
import random

# References
    # 1) https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python

# Functions
# Gets input from user
def getInput(question):
    hold = True
    while (hold):
        try:
            temp = int(input(question))
            if (temp <= 0):
                print("Value must be positive.")
                continue
        except ValueError:
            print("The value you entered is invalid. Please enter an integer.")
        else:
            hold = False
    return temp

# Main
fileName = "randomnum.txt"

amountRandomNums = getInput("How many random numbers do you want: ")
lowerBound = getInput("What is the lowest the random number should be: ")
upperBound = getInput("What is the highest the random number should be: ")

# Open File
try:
    fp = open(fileName, 'w')
    
# Checks if file was opened correctly
except OSError:
    print("Could not open file:", fileName)
    sys.exit()

# If file opened correctly, adds random numbers to file
with fp:
    for i in range(amountRandomNums):
        fp.write(str(random.randint(lowerBound, upperBound)) + "\n")
    fp.close()
