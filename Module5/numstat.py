# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Random Read
# Module 5

# Imports
import math
import random


# Main
repeat = True
while (repeat):
    # Initialize Variables
    currentVal = 0
    count = 0
    maxVal = 0
    minVal = 0
    totalSum = 0
    totalRange = 0
    average = float(0)

    # Runs code if file is opened correctly
    try:
        fileName = input("Please enter the file name: ")

        fp = open(fileName, "r")

        # Iterates through every number in the file
        for number in fp:
            currentVal = int(number)

            if (count == 0):
                maxVal = currentVal
                minVal = currentVal

            count += 1
            
            if (currentVal > maxVal):
                maxVal = currentVal
            
            if (currentVal < minVal):
                minVal = currentVal

            totalSum = totalSum + currentVal

        fp.close()

        average = float(totalSum/count)
        totalRange = maxVal - minVal

    # Prints error if file is not opened correctly
    except Exception as error:
        print(fileName, "could not be opened correctly")
        print("The error that occurred is", error)

    # Prints out all the calculated values
    else:
        print("File Name:", fileName)
        print("Sum:", totalSum)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maxVal)
        print("Minimum:", minVal)
        print("Range:", totalRange)

        # Asks user if they want to do another calculation
        doRepeat = input("Would you like to evaluate another file? (y/n): ")
        if (doRepeat != "y"):
            repeat = False
