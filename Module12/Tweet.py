# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Tweet Manager
# Module 12

# Tweet.py

# Imports
from datetime import datetime
import time
import math

# Tweet Class
class Tweet:
    def __init__(self, __author, __text):
        self.__author = __author
        self.__text = __text
        self.__age = time.time()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        currentTime = time.time()
        
        newAge = currentTime - self.__age

        if (newAge > 3600):
            ageString = str(math.floor(newAge / 3600))
            ageString += "h"
            return ageString
        elif (newAge > 60):
            ageString = str(math.floor(newAge / 60))
            ageString += "m"
            return ageString
        else:
            ageString = str(math.floor(newAge))
            ageString += "s"
            return ageString