# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Animal Generator Extended
# Module 10

# Imports
import math
import random
import os

import Animal

# Functions
    # Creates a new occurance of the Animal Class
def createAnimal():
    print("Would you like to create a mammal or a bird?")
    print("1. Mammal")
    print("2. Bird")
    animalClass = input("Which would you like to create? ")

    num = random.randint(1, 3)
    if (num == 1):
        mood = "happy"
    elif (num == 2):
        mood = "hungry"
    else:
        mood = "sleepy"

    # Gets Mammal
    if (animalClass == "1"):
        animalType = input("\nWhat type of mammal would you like to create? ")
        name = input("What is the mammal's name? ")
        hairColor = input("What color is the mammal's hair? ")

        newAnimal = Animal.Mammal(animalType, name, mood, hairColor)
    # Gets Bird
    else:
        animalType = input("\nWhat type of bird would you like to create? ")
        name = input("What is the bird's name? ")
        canFly = input("Can the bird fly? ")

        newAnimal = Animal.Bird(animalType, name, mood, canFly)

    return newAnimal

# Main
Animals = []

print("Welcome to the animal generator!")
print("This program creates animal objects.\n")

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