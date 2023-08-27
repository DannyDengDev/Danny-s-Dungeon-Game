from char_select_intro import *
from combat import * 
from enemies import * 
from world import *
from inventory import * 
from time_utils import * 

name = intro()
your_class = char_select(name)
current_location = Grasslands()
time = 12 # hours since game start
time_since_enemy_levelup = 1
hours_to_enemy_levelup = 24
enemy_level = 0

while True:
    location_intro(current_location)
    text, current_location = location_options(current_location)
    enemy_level = int(time / hours_to_enemy_levelup)
        # print("\nThe enemies of this world grow stronger!!!!!!!!!!!!!!!!!!!\n")
    for enemy in current_location.enemies:
            levels_needed = enemy_level - enemy.level
            for i in range(0, levels_needed):
                enemy.level_up()
    if text == "PROFILE": 
        profile_options(your_class, None, None)
        print_time(time)
        time += 0.5
    if text == "EXIT": print("EXITING GAME"); break
    if text == "REST": 
        # minimum/maximum hours
        # min = 1, max = 8 how does that conver to % hp, how do we heal % hp and % energy
        rest_hours = int(input("How many hours would you like to rest (1-8)?"))
        rest_hours = min(8, rest_hours)
        rest_hours = max(1, rest_hours)
        print("Resting... " + str(rest_hours) + " hours")
        # 
        your_class.gain_hp(your_class.max_health / 8 * rest_hours)
        your_class.change_energy(your_class.max_energy / 8 * rest_hours)
        time += rest_hours
    if text == "CHECK": 
        random_check = 1 #random.randint(0, 3)
        if random_check == 0:
            print("Discovered item: ") # TODO FILL IN ITEM
        elif random_check == 1:
            print("Checking area for enemies...")
            if is_day(time):
                new_enemy = current_location.enemies[random.randint(0, len(current_location.enemies) - 1)]
                new_enemy.health = new_enemy.max_health
            else:
                new_enemy = current_location.night_enemies[random.randint(0, len(current_location.night_enemies) - 1)]
                new_enemy.health = new_enemy.max_health
            victory = enter_combat(your_class, [new_enemy])
            if not victory:
                print("Game over... try again.")
                break
            time += 2
        elif random_check == 2:
            surrounding_areas = [x() for x in current_location.connecting_locations]
            print("You see the " + str([x.name for x in surrounding_areas]))
            time += 0.5
        


#When entering a new area, must check surrounding first
#enter_combat(your_class, [Bear(), Wolf()])
#Meat can be used in combat to heal
#pelts can be sold to merchants