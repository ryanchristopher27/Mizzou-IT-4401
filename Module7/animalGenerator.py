# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Animal Generator
# Module 7

# Imports
import math
import random
import os

import Animal

# Functions
    # Creates a new occurance of the Animal Class
def createAnimal():
    animalType = ""
    animalName = ""
    animalMood = ""
    animalType = input("\nWhat type of animal would you like to create? ")
    name = input("What is the animal's name? ")
    num = random.randint(1, 3)
    if (num == 1):
        mood = "happy"
    elif (num == 2):
        mood = "hungry"
    else:
        mood = "sleepy"

    newAnimal = Animal.Animal(animalType, name, mood)

    return newAnimal

# Main
Animals = []

print("Welcome to the animal generator!")
print("This program creates animal objects.")

repeat = True
# Continues to have user create Animals until he wishes to stop
while (repeat):
    userAnimal = createAnimal()

    Animals.append(userAnimal)

    # Asks user if they want to create another animal
    doRepeat = input("\nWould you like to add more animals? (y/n): ")
    if (doRepeat != "y"):
        repeat = False

print("\nAnimal List:")

# Prints out all the animals that the user created
i = 0
for i in range(len(Animals)):
    tempAnimal = Animals[i]
    print(tempAnimal.get_name() + " the " + tempAnimal.get_animal_type() + " is " + tempAnimal.check_mood())
