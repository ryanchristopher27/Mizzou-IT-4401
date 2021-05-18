# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Final Project

#Tic Tac Toe

# Imports
import math
import random
import os

# Functions
#Prints the Tic Tac Toe Board with passed values
def printBoard(totalMoves):

    print("\n " + totalMoves[0] + " | " + totalMoves[1] + " | " + totalMoves[2])
    print("-----------")
    print(" " + totalMoves[3] + " | " + totalMoves[4] + " | " + totalMoves[5])
    print("-----------")
    print(" " + totalMoves[6] + " | " + totalMoves[7] + " | " + totalMoves[8] + "\n")

# Prints the start menu and gets the 2 players names
def startMenu():
    print("\nWelcome to Tic Tac Toe")
    print("This is a 2-player game")
    
    player1 = input("\nPlayer 1, please enter your name: ")
    player2 = input("\nPlayer 2, please enter your name: ")

    print("\nHello " + player1 + " & " + player2 + "!")
    print("Let's play Tic-Tac-Toe\n")

    return player1, player2

# Plays the Tic Tac Toe game between the 2 players and returns the winner
def playGame(totalMoves, p1, p2, gameNum):
    roundNum = 0
    winner = False
    tie = False
    win = ""

    while(True):
        if (roundNum%2 == 0):
            p1Move = getPlayerMove(p1, totalMoves)
            totalMoves = enterPlayerMove(totalMoves, p1Move, "X")
            printBoard(totalMoves)
            winner = checkWinner(totalMoves, "X")
            if (winner == True):
                print(p1 + " has won the game!")
                win = "p1"
                break
        else:
            p2Move = getPlayerMove(p2, totalMoves)
            totalMoves = enterPlayerMove(totalMoves, p2Move, "O")
            printBoard(totalMoves)
            winner = checkWinner(totalMoves, "O")
            if (winner == True):
                print(p2 + " has won the game!")
                win = "p2"
                break

        tie = checkBoardFull(totalMoves)
        if (tie == True):
            print("\nIt's a Tie!")
            win = "tie"
            break
            
        roundNum += 1

    return win

# Loads prior player data if they have played before
def loadData(fileName, p1, p2):
    p1wins = 0
    p1losses = 0
    p1ties = 0
    p2wins = 0
    p2losses = 0
    p2ties = 0

    fp = open(fileName)
    fileLines = fp.readlines()
    fp.close()

    i = 0
    for line in fileLines:
        line = line.strip("\n")
        if (line == p1):
            p1wins = int(fileLines[i+1])
            p1losses = int(fileLines[i+2])
            p1ties = int(fileLines[i+3])
        elif (line == p2):
            p2wins = int(fileLines[i+1])
            p2losses = int(fileLines[i+2])
            p2ties = int(fileLines[i+3])
        i += 1

    return p1wins, p1losses, p1ties, p2wins, p2losses, p2ties

# Saves the data from the 2 players from the game into a file   
def saveData(fileName, player, wins, losses, ties):
    fp = open(fileName, "r")
    fileLines = fp.readlines()
    fp.close()

    found = False
    i = 0
    for line in fileLines:
        if (line == player + "\n"):
            fileLines[i+1] = str(wins) + "\n"
            fileLines[i+2] = str(losses) + "\n"
            fileLines[i+3] = str(ties) + "\n"
            found = True
        i += 1

    if (found):
        fp = open(fileName, "w")
        fp.writelines(fileLines)
        fp.close()
    else:
        fp = open(fileName, "a")
        fp.write(player + "\n")
        fp.write(str(wins) + "\n")
        fp.write(str(losses) + "\n")
        fp.write(str(ties) + "\n")
        fp.close()

# Gets the desired move from the player and returns it
def getPlayerMove(player, totalMoves):
    print(player + ", enter the number that corresponds where you would like to play.")
    baseValues = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    printBoard(baseValues)

    # Makes sure value is not already used
    while(True):
        choice = input("\nEnter value here: ")
        try:
            if (int(choice) < 1 or int(choice) > 9):
                print("\nPlease enter a valid input")
            elif (totalMoves[int(choice) - 1] == " "):
                break
            else:
                print("\nSpot is already taken")
        except ValueError:
            print("\nPlease enter an integer")

    return choice

# Enters the player move into the moves array
def enterPlayerMove(totalMoves, move, player):
    if (player == "X"):
        totalMoves[int(move) - 1] = "X"
    else:
        totalMoves[int(move) - 1] = "O"

    return totalMoves

# Checks the board to see if there is a winner
def checkWinner(totalMoves, playerValue):
    win = False
    if (totalMoves[0] == totalMoves[1] == totalMoves[2] == playerValue):
        win = True
    elif (totalMoves[3] == totalMoves[4] == totalMoves[5] == playerValue):
        win = True
    elif (totalMoves[6] == totalMoves[7] == totalMoves[8] == playerValue):
        win = True
    elif (totalMoves[0] == totalMoves[3] == totalMoves[6] == playerValue):
        win = True
    elif (totalMoves[1] == totalMoves[4] == totalMoves[7] == playerValue):
        win = True
    elif (totalMoves[2] == totalMoves[5] == totalMoves[8] == playerValue):
        win = True
    elif (totalMoves[0] == totalMoves[4] == totalMoves[8] == playerValue):
        win = True
    elif (totalMoves[2] == totalMoves[4] == totalMoves[6] == playerValue):
        win = True

    return win

# Checks the board to see if it is full
def checkBoardFull(totalMoves):
    full = False
    count = 0
    for x in totalMoves:
        if (x != " "):
            count += 1
    
    if (count == 9):
        full = True

    return full

# Prints the end menu and gets the input from the user and returns it
def printEndMenu(p1, p2):
    selection = 0
    while (True):
        print("\n1. Play Again");
        print("2. View Player1 Statistics (" + p1 + ")")
        print("3. View Player2 Statistics (" + p2 + ")")
        print("4. Quit")
        selection = input("\nEnter your selection: ")
        try:
            if (int(selection) > 0 and int(selection) < 5):
                break
            print("\nPlease select a valid option")
        except ValueError:
            print("\nPlease enter a numeric value")

    return selection

# Prints the stats of the desired player
def printStats(player, wins, losses, ties):
    print("\nPlayer Stats")
    print("------------")
    print("Name: " + player)
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))
    if ((wins + losses) == 0):
        print("Win/Loss Ratio: No wins or losses")
    else:
        print("Win/Loss Ratio: " + str(round(wins/(wins+losses), 2)))

# Main Function
def main():
    gameNum = 0
    totalMoves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    winner = ""
    p1wins = 0
    p1losses = 0
    p1ties = 0
    p2wins = 0
    p2losses = 0
    p2ties = 0
    fileName = "ticTacToe.txt"

    p1, p2 = startMenu()

    p1wins, p1losses, p1ties, p2wins, p2losses, p2ties = loadData(fileName, p1, p2)

    selection = "1"
    while(True):
        if (selection == "1"):
            win = playGame(totalMoves, p1, p2, gameNum)
            if (win == "p1"):
                p1wins += 1
                p2losses += 1
            elif (win == "p2"):
                p2wins += 1
                p1losses += 1
            else:
                p1ties += 1
                p2ties += 1
            selection = printEndMenu(p1, p2)
            totalMoves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        elif (selection == "2"):
            printStats(p1, p1wins, p1losses, p1ties)
            selection = printEndMenu(p1, p2)
        elif (selection == "3"):
            printStats(p2, p2wins, p2losses, p2ties)
            selection = printEndMenu(p1, p2)
        else:
            saveData(fileName, p1, p1wins, p1losses, p1ties)
            saveData(fileName, p2, p2wins, p2losses, p2ties)
            break;

    print("\n" + p1 + " & " + p2 + ", thanks for playing Tic-Tac-Toe!")


# Main Call
main()