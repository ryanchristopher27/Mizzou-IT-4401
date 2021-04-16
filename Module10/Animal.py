# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Animal Generator Extended
# Module 10

# File: Animal Class File with Mammal and Bird Subclasses

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


class Mammal(Animal):
    def __init__(self, __animal_type, __name, __mood, __hair_color):
        super().__init__(__animal_type, __name, __mood)
        self.__hair_color = __hair_color

    def get_hair_color(self):
        return self.__hair_color

class Bird(Animal):
    def __init__(self, __animal_type, __name, __mood, __can_fly):
        super().__init__(__animal_type, __name, __mood)
        self.__can_fly = __can_fly

    def get_can_fly(self):
        return self.__can_fly