# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Animal Generator
# Module 7

# File: Animal Class File

# Class
class Animal:
    def __init__(self, __animal_type, __name, __mood):
        self.__animal_type = __animal_type
        self.__name = __name
        self.__mood = __mood

    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def check_mood(self):
        return self.__mood