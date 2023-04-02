import random
import math
from classes import *

def intro():
    print("\/"*20)
    print("WELCOME TO DUNGEON DYNAMICS!!!")
    print("/\\"*20)
    return input("Please enter your characters name: ")

def char_select(char_name):
    
    print("Welcome " + char_name + ", please choose a class from the list: ")

    scout_character = Scout()
    print("1. Scout:")
    scout_character.print_stats()
    print()

    fighter_character = Fighter()
    print("2. Fighter:")
    fighter_character.print_stats()
    print()

    mage_character = ApprenticeMage()
    print("3. Apprentice Mage:")
    mage_character.print_stats()
    print()

    archer_character = Archer()
    print("4. Archer:")
    archer_character.print_stats()
    print()

    character_choice = int(input("Enter the number for your chosen class: "))

    if character_choice == 1:
        your_class = Scout()
        print("You have chosen the Scout!")

    if character_choice == 2:
        your_class = Fighter()
        print("You have chosen the Fighter!")

    if character_choice == 3:
        your_class = ApprenticeMage()
        print("You have chosen the Apprentice Mage!")

    if character_choice == 4:
        your_class = Archer()
        print("You have chosen the Archer!")
    print("Hmmm.... Excellent choice!")
    your_class.name = char_name
    return your_class