import math
import random
import skills
from inventory import * 

def speed_diff_calculator(speed1, speed2):
    # return % miss or % escape ~
    return None 

def check_and_remove_dead_enemies(combatants):
    # combatants = [(speed, main character), (speed, wolf), (speed, bear), etc...]
    dead_combatants = []
    for i in range(0, len(combatants)):
        char = combatants[i]
        if char.health <= 0:
            dead_combatants.append(i)
    for j in dead_combatants:
        combatants.pop(j)

def enter_combat(main_character, enemies):
    print()
    print("\/"*20)
    for enemy in enemies: 
        print("Started combat with " + str(enemy))
    print("/\\"*20)
    print()
    combatants = [main_character]
    [combatants.append(enemy) for enemy in enemies]
    def get_speed(x):
        return x.speed
    combatants.sort(key=get_speed, reverse=True)


    # main combat 
    turn_index = 0
    ally_modifiers = []
    enemy_modifiers = []
    ally_modifier_durations = []
    enemy_modifier_durations = []
    # modifier_duration_queue = []
    # while there is only one allegiance left (WIP)
    while len(combatants) > 1:
        
        current_combatant = combatants[turn_index % len(combatants)]

        ### ALL COMBAT HAPPENS HERE \/

        # increment turn count
        correct_turn = 1 + math.ceil(turn_index / len(combatants))
        
        if current_combatant.allegiance == "Main Character":
            print("TURN: " + str(correct_turn))
            modifier = display_options(main_character, combatants, ally_modifiers)
            if type(modifier) is str:
                if modifier is "ESCAPE TRUE":
                    print(main_character.name + " was able to escape!")
                    return True
                else:
                    print(main_character.name + " could not escape!")
            else: 
                if modifier:
                    new_ally_modifiers, new_enemy_modifiers = modifier["function"]()
                    if new_ally_modifiers: 
                        ally_modifiers.append(new_ally_modifiers)
                        ally_modifier_durations.append([new_ally_modifiers, modifier['ally_duration']])
                    if new_enemy_modifiers: 
                        enemy_modifiers.append(new_enemy_modifiers)
                        enemy_modifier_durations.append([new_enemy_modifiers, modifier['enemy_duration']])
                    
            for idx in range(0, len(ally_modifier_durations)): 
                ally_modifier_durations[idx][1] -= 1
            ally_durations_to_remove = []
            for idx in range(0, len(ally_modifier_durations)): 
                if ally_modifier_durations[idx][1] == 0:
                    ally_durations_to_remove.append(idx)
                    ally_modifiers.remove(ally_modifier_durations[idx][0])
            # if new_modifiers:
            #     modifiers.append(new_modifiers)
        else:
            enemy_attack(current_combatant, combatants, main_character, enemy_modifiers)

            # change duration of all modifiers after each round of combat

            for idx in range(0, len(enemy_modifier_durations)): 
                enemy_modifier_durations[idx][1] -= 1

            # take out modifiers with 0 duration left 
            
            enemy_durations_to_remove = []

            # for idx in ally_durations_to_remove:

            for idx in range(0, len(enemy_modifier_durations)): 
                if enemy_modifier_durations[idx][1] == 0:
                    enemy_durations_to_remove.append(idx)
                    enemy_modifiers.remove(enemy_modifier_durations[idx][0])



        ### ALL COMBAT HAPPENS HERE /\
        check_and_remove_dead_enemies(combatants)

        turn_index += 1
        
    # AFTER COMBAT \/    
    print(combatants[0].name + " WAS VICTORIOUS!!!")
    victory = main_character.name == combatants[0].name
    return victory

    
    # [a, b, c] - list 
    # (1, 2, 3) - tuple
    # (random # for speed , main_character)

    # introduce the combatants
    # decide whose turn is first based on speed diff
    # on each turn: 
    #  - use item       => items in inventory as options
    #  - attack         => deal your attack to enemy
    #  - block          => Lowers damage taken for one turn, chance to stun
    #  - use ability    => use ability (with chance to miss?) on enemy
    #  - escape         => Chance to escape, can't escape on bosses, based on speed?


def targetting(main_character, combatants):
    print("\n\nTarget options are: ")
    char_index = 1
    for char in combatants:
        if char.allegiance !="Main Character":
            print(str(char_index) + ".  " + char.name + "    HP: " + str(round(char.health)))
            char_index += 1
    return input("\nEnter # of target you'd like to attack: ")

def item_options(main_character, combatants, modifiers):
    print_inventory(INVENTORY)
    item_target = int(input("\nEnter # of the item you'd like to use/equip: ")) - 1
    item_to_use = INVENTORY[item_target]
    if item_to_use["type"] == "FOOD":
        main_character.gain_hp(item_to_use["hp"])
        remove_item(INVENTORY, item_to_use)
    if item_to_use["type"] == "WEAPON":
        main_character.equip_item(item_to_use, INVENTORY)
        remove_item(INVENTORY, item_to_use)
    return display_options(main_character, combatants, modifiers)

def check_death(main_character, target):
    # kills enemy and grants xp 
    if target.health <= 0:
        print(main_character.name + " defeated " + target.name)
        print(main_character.name + " gained " + str(target.exp_granted) + " XP!")
        main_character.gain_xp(target.exp_granted)

        # get loot
        if len(target.loot) > 0:
            random_drop = target.loot[random.randint(0, len(target.loot) - 1)] 
            add_item_to_inventory(INVENTORY, random_drop)
        return True
    return False

def pick_target(main_character, combatants):
    target_index = int(targetting(main_character, combatants))
    target = None
    char_index = 1
    for char in combatants:
        #print(char)
        if char.allegiance != "Main Character":
            if char_index == target_index:
                target = char
            char_index += 1
    return target

def apply_dot(source, target, damage, duration, origin):
    target.statuses.append({
        "type" : "dot",
        "damage" : damage,
        "duration" : duration,
        "origin" : origin
    })

def instant_cast(main_character, combatants, modifiers, skill):
    target = pick_target(main_character, combatants)
    #print_damage(main_character, target, main_character.base_damage)
    print("="*20)
    print(main_character.name + " used " + skill['name'] + " on " + target.name)
    for i in range(0, skill['num_casts']):
        # modifies base damage
        base_damage = skill['damage']
        if skill['incl_base']: 
            base_damage += main_character.base_damage
        modified_damage = base_damage + round(main_character.current_level * skill['level_scaling'])

        # prints damage
        print(main_character.name + " did " + str(modified_damage) + " to " + target.name)
        print(target.name + " HP " + str(round(target.health)) + " => " + str(round(target.health - modified_damage)))
        target.health -= modified_damage

        if check_death(main_character, target): break
    if skill['dot']:
        dot_damage = skill['damage'] + round(main_character.current_level * skill['level_scaling'])
        apply_dot(main_character, target, dot_damage, skill['enemy_duration'], skill['name'])
        return skill
    return skill

def attack_options(main_character, combatants, modifiers):

    target = pick_target(main_character, combatants)
    #print_damage(main_character, target, main_character.base_damage)
    print("="*20)

    # modifies base damage
    base_damage = main_character.base_damage + main_character.bonus_damage
    print(modifiers)
    if modifiers:
        modified_damage = base_damage
        for modifier in modifiers:
            modified_damage = modifier(base_damage)
    else:
        modified_damage = base_damage

    # prints damage
    deal_damage(main_character, target, modified_damage)


    # your character did X base damage to other character
    # your character did X additional damage to other character
    # other character hp 100 => 90
  
    return None

def deal_damage(source, target, damage):
    damage_line(source.name, target.name, damage, target.health)
    target.health -= damage
    return check_death(source, target)

def enemy_attack(enemy, combatants, main_character, modifiers):
    for status in enemy.statuses: 
        if status['type'] is 'dot':
            if status['duration'] == 0:
                enemy.statuses.remove(status)
            else:
                print(enemy + " is affected by " + status["origin"] + " for " + str(status['duration']) + " more turns.")
                if deal_damage(main_character, enemy, status["damage"]): return None
                status['duration'] -= 1
    valid_combatants = []
    for char in combatants:
        #print(char)
        if char.allegiance is not enemy.allegiance:
            valid_combatants.append(char)
    
    target_index = random.randint(0, len(valid_combatants) - 1)
    target = valid_combatants[target_index]
    print("="*20)
    modified_damage = enemy.base_damage
    if modifiers:
        for modifier in modifiers:
            modified_damage = modifier(modified_damage)
    else:
        modified_damage = enemy.base_damage
    damage_line(enemy, target.name, modified_damage, target.health)
    target.health -= modified_damage
  
    return None

def damage_line(source_name, target_name, damage, target_hp):
    print(str(source_name) + " did " + str(damage) + " to " + str(target_name))
    print(target_name + " HP " + str(round(target_hp)) + " => " + str(round(target_hp - damage)))

def block_options(main_character, combatants, modifiers):
    # TODO DANNY HW
    return None

def ability_options(main_character, combatants, modifiers):
    
    # print out skills
    main_character.print_skills()

    ## ask player to select what # skill they want to use
    skill_target = int(input("\nEnter # of the skill you'd like to use: ")) - 1
    
    # get skill object from character
    skill = main_character.skills[skill_target]

    # check energy cost
    if main_character.energy < skill['cost']:
        print('You do not have enough energy.' + skill['name'] + ' costs ' + str(skill['cost']) + ' energy and you have ' + str(main_character.energy) + ' energy')
        return display_options(main_character, combatants, modifiers)

    # change current energy
    main_character.change_energy(-1 * skill["cost"])
    if skill["instant_cast"]:
        #  perform instant cast ability here 
        return instant_cast(main_character, combatants, modifiers, skill)
    else:
        return skill

def escape_options(main_character, combatants, modifiers):
    for enemy in combatants: 
        if main_character.speed < enemy.speed:
            return "ESCAPE_FALSE"
    return "ESCAPE_TRUE"

def profile_options(main_character, combatants, modifiers):
    print("Your profile: ")
    print("HP: " + str(round(main_character.health)) + "/" + str(round(main_character.max_health)))
    print("Energy: " + str(main_character.energy) + "/" + str(main_character.max_energy))
    print("Base Damage: " + str(main_character.base_damage))
    print("Bonus Damage: " + str(main_character.bonus_damage))
    print("Base Defense: " + str(main_character.defense))
    print("Bonus Defense: " + str(main_character.bonus_defense))
    
    print("Lvl: " + str(main_character.current_level))
    print("XP: " + str(main_character.current_xp) + "/" + str(main_character.xp_to_next_level))
    print_inventory(INVENTORY)
    main_character.print_gear()
    if combatants is None and modifiers is None: return None
    return display_options(main_character, combatants, modifiers)
    

def display_options(main_character, combatants, modifiers):
    print("\nTurn options: ")
    print("1. Items")
    print("2. Attack")
    #print("3. Block")
    print("3. Use Ability")
    print("4. Escape")
    print("5. Profile")
    player_choice = int(input("\nEnter what # move you'd like to make?")) - 1
    all_options = [item_options, attack_options, ability_options, escape_options, profile_options]
    return all_options[player_choice](main_character, combatants, modifiers)
    # TODO Items function
    # TODO Attack function
    # TODO Block function
    # TODO Use ability function
    # TODO EScape
    # targetting(main_character, combatants)

# def block

def print_damage(char1, char2, damage):
    # %[flags][width][.precision]type 
    print("{0: <10} did {0: <5} damage to {0: <10}".format(char1.name, damage, char2.name))
    #print("{0: <10} HP {0: <5} => {0: <10}".format(char2.name, char2.health, char2.name))
    # print(main_character.allegiance + " did " + str(main_character.base_damage) + " to " + target.name)
    # print(target.name + " HP " + str(target.health) + " => " + str(target.health - main_character.base_damage))