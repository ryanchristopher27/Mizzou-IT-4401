# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Number Stats 2
# Module 6

# Imports
import math
import random
import os

# Functions
# Sorts an array into increasing order
def sort(intArray):
    counter = len(intArray)

    i = 0
    j = 0
    for i in range (counter):
        for j in range (counter-1):
            if(intArray[j] > intArray[j+1]): 
                intArray[j], intArray[j+1] = intArray[j+1], intArray[j]

# Calculates the median of a given array of integers
# Returns the median
def findMedian(intArray):
    counter = len(intArray)
    halfCounter = int(counter / 2)

    if (counter % 2 == 0):
        hold1 = intArray[halfCounter]
        hold2 = intArray[halfCounter-1]
        median = float((hold1 + hold2)/2)
    else:
        median = intArray[halfCounter]

    return median

# Calculates the mode of a given array of integers
# Returns an array of all mode values
def findMode(intArray):
    numCount = {}
    mode = []
    maxCount = 0

    for number in intArray:
        if number in numCount:
            numCount[number] += 1
        else:
            numCount[number] = 1

    for number in numCount:
        if (numCount[number] > maxCount):
            maxCount = numCount[number]

    for number in numCount:
        if (numCount[number] == maxCount):
            mode.append(number)

    return mode

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
    median = float(0)
    mode = []
    numsArr = []

    # Runs code if file is opened correctly
    try:
        fileName = input("Please enter the file name: ")

        fp = open(fileName, "r")

        # Iterates through every number in the file
        for number in fp:
            currentVal = int(number)

            numsArr.append(currentVal)

            if (count == 0):
                maxVal = currentVal
                minVal = currentVal

            count += 1;
            
            if (currentVal > maxVal):
                maxVal = currentVal
            
            if (currentVal < minVal):
                minVal = currentVal

            totalSum = totalSum + currentVal

        fp.close()

        average = float(totalSum/count)
        totalRange = maxVal - minVal

        sort(numsArr)

        median = findMedian(numsArr)
        mode = findMode(numsArr)

    # Prints error if file is not opened correctly
    except Exception as error:
        if (os.path.getsize(fileName) == 0):
            print("There are no numbers in", fileName)
        else:
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
        print("Median:", median)
        print("Mode:", mode)

        # Asks user if they want to do another calculation
        doRepeat = input("Would you like to evaluate another file? (y/n): ")
        if (doRepeat != "y"):
            repeat = False
