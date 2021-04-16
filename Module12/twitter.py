# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Tweet Manager
# Module 12

# Twitter.py

# Imports
import math
import random
import os
import Tweet

# Functions
def makeTweet():
    tooLong = True

    tempName = input("\nWhat is your name? ")

    while (tooLong):
        tempTweet = input("What would you like to tweet? ")
        if (len(tempTweet) < 140):
            tooLong = False
        else:
            print("\nTweets can only be 140 characters!\n")

    tweet = Tweet.Tweet(tempName, tempTweet)

    tempName += ","

    print(tempName, "your tweet has been saved.")

    return tweet

def displayTweet(tweet):
    author = tweet.get_author()
    text = tweet.get_text()
    age = tweet.get_age()

    print(author, "-", age)
    print(text)

def viewRecentTweets(tweetArray):
    print("\nRecent Tweets")
    print("-------------")
    if (tweetArray):
        for tweet in tweetArray[::-1]:
            displayTweet(tweet)
            print("")
    else:
        print("There are no recent tweets.")

def searchTweets(tweetArray):
    successful = False
    foundTweets = []

    if (tweetArray):

        searchText = input("What would you like to search for? ")

        for tweet in tweetArray:
            text = tweet.get_text()
            if (searchText in text):
                foundTweets.append(tweet)
                successful = True

        if (successful):
            print("\nSearch Results")
            print("--------------")
            for tweet in foundTweets[::-1]:
                displayTweet(tweet)
                print("")
        else:
            print("\nNo tweets contained", searchText)
    else:
        print("\nThere are no tweets to search")

# Main Function
def main():
    Tweets = []

    selection = 0
    while (selection != "4"):
        print("\nTweet Menu")
        print("----------")
        print("1. Make a Tweet")
        print("2. View Recent Tweet")
        print("3. Search Tweet")
        print("4. Quit\n")

        repeat = True
        while (repeat):
            selection = input("What would you like to do? ")

            if (selection == "1"):
                # Make Tweet
                tweet = makeTweet()
                Tweets.append(tweet)
                repeat = False
            elif (selection == "2"):
                # View Recent Tweets
                viewRecentTweets(Tweets)
                repeat = False
            elif (selection == "3"):
                # Search Tweet
                searchTweets(Tweets)
                repeat = False
            elif (selection == "4"):
                # Quit
                repeat = False
            else:
                try:
                    val = int(selection)
                    print("\nPlease select a valid option\n")
                except ValueError:
                    print("\nPlease enter a numeric value.\n")
    
    print("\nThank you for using the Tweet Manager!")

main()