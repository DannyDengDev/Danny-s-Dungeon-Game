from locations import *
from combat import *

def location_intro(location):
    print("\nYou are at " + location.name + ".")
    print(location.description)

def location_options(location):
    print("\nTravel options: ")
    print("1. Check surroundings")
    print("2. Rest")
    print("3. Travel elsewhere")
    print("4. Check profile")
    print("5. Exit game")
    player_choice = int(input("\nEnter what # option you'd like to make?")) - 1
    all_options = [check_surroundings, rest, travel_elsewhere, check_profile, exit_game]
    return all_options[player_choice](location)

def check_profile(location):
    # check player profile
    return ("PROFILE", location)

def check_surroundings(location):
    # either find enemies or allies
    return ("CHECK", location)

def rest(location):
    # heals the player and passes time
    return ("REST", location)

def travel_elsewhere(location):
    # give options to travel to connecting areas
    for i, location_choice in enumerate(location.connecting_locations):
        location_choice_ob = location_choice()
        print(str(i + 1) + "." + location_choice_ob.name)
    player_choice = int(input("\nEnter what # option you'd like to make?")) - 1
    player_travel_choice = location.connecting_locations[player_choice]
    player_travel_choice_ob = player_travel_choice()
    print("Traveling to " + player_travel_choice_ob.name)
    return ("TRAVEL", player_travel_choice_ob)
    
def exit_game(location):
    # exit game (SAVE PROGRESS?)
    return ("EXIT", location)