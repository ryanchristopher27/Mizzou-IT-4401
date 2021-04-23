# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Rock, Paper, Scissors
# Module 13

# rps.py

# Imports
import math
import random
import os

# Functions
# Prints the menu and returns the input of the user
def printAndGetMenuInput():
    print("Welcome to Rock, Paper, Scissors!\n")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("\nEnter choice: ")

    return choice

# Prints the second menu and returns the input of the user
def printAndGetSecondMenuInput():
    print("\nWhat would you like to do?\n")
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit")

    choice = input("\nEnter choice: ")

    return choice

# Starts a new game with a new user
def startNewGame(name, wins, losses, ties):
    cont = True

    name = input("\nWhat is your name? ")

    print("\nHello " + name + ". Let's play!")

    name, wins, losses, ties = play(name, wins, losses, ties)

    # Repeats until user enters a valid input
    while (True):
        gameChoice = printAndGetSecondMenuInput()

        if (gameChoice == "1"):
            # New Game
            name, wins, losses, ties = play(name, wins, losses, ties)
        elif (gameChoice == "2"):
            # Load Game
            print("\n" + name + ", here are your game play statistics...")
            print("\nWins: " + str(wins))
            print("Losses: " + str(losses))
            print("Ties: " + str(ties))
            print("Win/Loss Ratio: " + str(wins/(wins+losses)))
        elif (gameChoice == "3"):
            # Quit
            cont = False
            print("\n" + name + ", your game has been saved.")
            break;
        else:
            try:
                val = int(gameChoice)
                print("\nPlease select a valid option\n")
            except ValueError:
                print("\nPlease enter a numeric value.\n")

    return name, wins, losses, ties, cont

# Starts a game that already has user data
def startLoadGame(fileName, name, wins, losses, ties):
    cont = True

    name = input("\nWhat is your name? ")

    print("\nWelcome back " + name + ". Let's play!")

    # Reads the lines of the file into an array
    fp = open(fileName, "r")
    fileLines = fp.readlines()
    fp.close()

    # Updates the old data from the user with the new data
    i = 0
    for line in fileLines:
        # print("\n" + line)
        if (line == name + "\n"):
            # print("found")
            name = fileLines[i]
            wins = int(fileLines[i+1])
            losses = int(fileLines[i+2])
            ties = int(fileLines[i+3])
        i += 1

    name = name.rstrip("\n")

    name, wins, losses, ties = play(name, wins, losses, ties)

    # repeats until user enters a valid input
    while (True):
        menuChoice = printAndGetSecondMenuInput()

        if (menuChoice == "1"):
            # New Game
            name, wins, losses, ties = play(name, wins, losses, ties)
        elif (menuChoice == "2"):
            # Load Game
            print("\n" + name + ", here are your game play statistics...")
            print("\nWins: " + str(wins))
            print("Losses: " + str(losses))
            print("Ties: " + str(ties))
            print("Win/Loss Ratio: " + str(round(wins/(wins+losses), 2)))
        elif (menuChoice == "3"):
            # Quit
            cont = False
            print("\n" + name + ", your game has been saved.")
            break;
        else:
            try:
                val = int(menuChoice)
                print("\nPlease select a valid option\n")
            except ValueError:
                print("\nPlease enter a numeric value.\n")
    
    return name, wins, losses, ties, cont

# Performs the rock, paper, scissors gameplay and prints who won
# Returns all the newly updated info
def play(name, wins, losses, ties):
    round = getRounds(wins, losses, ties)

    print("\nRound " + str(round))

    while (True):
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors\n")
        
        choice = input("What will it be? ")

        computerChoice = random.randint(1, 3)

        if (choice == "1"):
            if (computerChoice == 1):
                print("\nYou chose Rock. The computer chose Rock. You Tie!")
                ties += 1
            elif (computerChoice == 2):
                print("\nYou chose Rock. The computer chose Paper. You Lose!")
                losses += 1
            else:
                print("\nYou chose Rock. The computer chose Scissors. You Win!")
                wins += 1
            break;
        elif (choice == "2"):
            if (computerChoice == 1):
                print("\nYou chose Paper. The computer chose Rock. You Win!")
                wins +=1
            elif (computerChoice == 2):
                print("\nYou chose Paper. The computer chose Paper. You Tie!")
                ties += 1
            else:
                print("\nYou chose Paper. The computer chose Scissors. You Lose!")
                losses += 1
            break;
        elif (choice == "3"):
            if (computerChoice == 1):
                print("\nYou chose Scissors. The computer chose Rock. You Lose!")
                losses += 1
            elif (computerChoice == 2):
                print("\nYou chose Scissors. The computer chose Paper. You Win!")
                wins += 1
            else:
                print("\nYou chose Scissors. The computer chose Scissors. You Tie!")
                ties += 1
            break;
        else:
            try:
                val = int(choice)
                print("\nPlease select a valid option")
            except ValueError:
                print("\nPlease enter a numerical value")

    return name, wins, losses, ties

# Saves the user data to the designated file and replaces the old data if the user has played before
def saveToFile(newUser, fileName, name, wins, losses, ties):

    if (newUser):
        # New user so append data to end of file
        fp = open(fileName, "a")

        fp.write(name)
        fp.write("\n")
        fp.write(str(wins))
        fp.write("\n")
        fp.write(str(losses))
        fp.write("\n")
        fp.write(str(ties))

        fp.close()
    else:
        # Returning user so replace old data with new data
        fp = open(fileName, "r")
        fileLines = fp.readlines()
        fp.close()

        i = 0
        for line in fileLines:
            if (line == name):
                #fileLines[i] = name
                fileLines[i+1] = str(wins) + "\n"
                fileLines[i+2] = str(losses) + "\n"
                fileLines[i+3] = str(ties) + "\n"
                break;
            i += 1
        fp = open(fileName, "w")
        fp.writelines(fileLines)
        fp.close()

# Returns the number of rounds as an int
def getRounds(wins, losses, ties):
    rounds = wins + losses + ties + 1
    return rounds

# Main Function
def main():
    # Declare variables
    userName = ""
    userWins = 0
    userLosses = 0
    userTies = 0
    cont = True

    while (cont):
        gameChoice = printAndGetMenuInput()

        if (gameChoice == "1"):
            # New Game
            userName, userWins, userLosses, userTies, cont = startNewGame(userName, userWins, userLosses, userTies)
            saveToFile(True, "rps.txt", userName, userWins, userLosses, userTies)
        elif (gameChoice == "2"):
            # Load Game
            userName, userWins, userLosses, userTies, cont = startLoadGame("rps.txt", userName, userWins, userLosses, userTies)
            saveToFile(False, "rps.txt", userName, userWins, userLosses, userTies)
        elif (gameChoice == "3"):
            # Quit
            print("\n" + userName + ", your game has been saved.")
            break;
        else:
            try:
                val = int(gameChoice)
                print("\nPlease select a valid option\n")
            except ValueError:
                print("\nPlease enter a numeric value.\n")


main()