# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Random Read
# Module 5

# Imports
import math
import random

# References
    # 1) https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

# Main
fileName = "randomnum.txt"
count = 1

# Open File
try:
    fp = open(fileName, "r")

# Checks if file was opened correctly
except OSError:
    print("Could not open file:", fileName)
    sys.exit()

# Prints all integers from the file
for line in fp:
    print(line.strip())
    count=count+1

print("\nRandom Number Count: " + str(count-1))

fp.close()
