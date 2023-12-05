'''
Classes
You are making a video game! The given code declares a Player class, with its attributes and an intro() method.
Complete the code to take the name and level from user input, create a Player object with the corresponding values and call the intro() method of that object.

Sample Input
Tony
12

Sample Output
Tony (Level 12)

Use the dot syntax to call the intro() method for the declared object.
'''

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here
# Taking user input for name and level
name_input = input()
level_input = input()

# Creating a Player object with user-input values
player_object = Player(name_input, level_input)

# Calling the intro() method of the Player object
player_object.intro()