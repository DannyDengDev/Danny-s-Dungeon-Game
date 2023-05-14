from char_select_intro import *
from combat import * 
from enemies import * 
from world import *
from inventory import * 

name = intro()
your_class = char_select(name)
current_location = Grasslands()
time = 0 # hours since game start


while True:
    location_intro(current_location)
    text, current_location = location_options(current_location)
    if text == "PROFILE": 
        print("Lvl: " + str(your_class.current_level))
        print("XP: " + str(your_class.current_xp) + " / " + str(your_class.xp_to_next_level))
        print("HP: " + str(your_class.health) + "/" + str(your_class.max_health))
        print_inventory(INVENTORY)
    if text == "EXIT": print("EXITING GAME"); break
    if text == "REST": 
        print("Resting...")
        your_class.gain_hp(100)
        time += 8
    else:
        time += 1
    if text == "CHECK": 
        random_check = 1 #random.randint(0, 3)
        if random_check == 0:
            print("Discovered item: ") # TODO FILL IN ITEM
        elif random_check == 1:
            print("Checking area for enemies...")
            new_enemy = current_location.enemies[random.randint(0, len(current_location.enemies) - 1)]
            new_enemy.health = new_enemy.max_health
            victory = enter_combat(your_class, [new_enemy])
            if not victory:
                print("Game over... try again.")
                break
        elif random_check == 2:
            surrounding_areas = [x() for x in current_location.connecting_locations]
            print("You see the " + str([x.name for x in surrounding_areas]))

#When entering a new area, must check surrounding first
#enter_combat(your_class, [Bear(), Wolf()])
#Meat can be used in combat to heal
#pelts can be sold to merchants