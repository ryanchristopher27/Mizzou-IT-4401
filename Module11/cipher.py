# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Cipher
# Module 11

# Imports
import math
import random
import os


# Functions
def encode(string):
    string = string.replace("a", "0")
    string = string.replace("b", "1")
    string = string.replace("c", "2")
    string = string.replace("d", "3")
    string = string.replace("e", "4")
    string = string.replace("f", "5")
    string = string.replace("g", "6")
    string = string.replace("h", "7")
    string = string.replace("i", "8")
    string = string.replace("j", "9")
    string = string.replace("k", "!")
    string = string.replace("l", "@")
    string = string.replace("m", "#")
    string = string.replace("n", "$")
    string = string.replace("o", "%")
    string = string.replace("p", "^")
    string = string.replace("q", "&")
    string = string.replace("r", "*")
    string = string.replace("s", "(")
    string = string.replace("t", ")")
    string = string.replace("u", "-")
    string = string.replace("v", "+")
    string = string.replace("w", "<")
    string = string.replace("x", ">")
    string = string.replace("y", "?")
    string = string.replace("z", "=")

    return string

def decode(string):
    string = string.replace("0", "a")
    string = string.replace("1", "b")
    string = string.replace("2", "c")
    string = string.replace("3", "d")
    string = string.replace("4", "e")
    string = string.replace("5", "f")
    string = string.replace("6", "g")
    string = string.replace("7", "h")
    string = string.replace("8", "i")
    string = string.replace("9", "j")
    string = string.replace("!", "k")
    string = string.replace("@", "l")
    string = string.replace("#", "m")
    string = string.replace("$", "n")
    string = string.replace("%", "o")
    string = string.replace("^", "p")
    string = string.replace("&", "q")
    string = string.replace("*", "r")
    string = string.replace("(", "s")
    string = string.replace(")", "t")
    string = string.replace("-", "u")
    string = string.replace("+", "v")
    string = string.replace("<", "w")
    string = string.replace(">", "x")
    string = string.replace("?", "y")
    string = string.replace("=", "z")

    return string


# Main
print("Welcome to the Secret Message Encoder/Decoder")

print("1. Encode a message")
print("2. Decode a message")
print("3. Exit")

selection = 0
stop = 0
while (stop == 0):

    repeat = 0
    while(repeat == 0):
        selection = input("\nWhat would you like to do? ")

        if (selection == "1"):
            string = input("\nEnter a message to encode: ")
            newString = encode(string)
            print("Encoded message: " + newString)
            repeat = 1
        elif (selection == "2"):
            string = input("\nEnter a message to decode: ")
            newString = decode(string)
            print("Decoded message: " + newString)
            repeat = 1
        elif (selection == "3"):
            stop = 1
            repeat = 1
        else:
            print(selection + " is not a valid choice.")





