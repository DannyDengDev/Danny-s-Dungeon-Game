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
        char = combatants[i][1]
        if char.health <= 0:
            dead_combatants.append(i)
    for j in dead_combatants:
        combatants.pop(j)

def enter_combat(main_character, enemies):
    print()
    print("\/"*20)
    for enemy in enemies: 
        print("Started combat with " + enemy.name)
    print("/\\"*20)
    print()
    combatants = [(random.randint(1, main_character.speed), main_character)] + [(random.randint(0, enemy.speed), enemy) for enemy in enemies]
    #combatants.sort(key=reverse=True)


    # main combat 
    turn_index = 0
    ally_modifiers = []
    enemy_modifiers = []

    # while there is only one allegiance left (WIP)
    while len(combatants) > 1:
        
        current_combatant = combatants[turn_index % len(combatants)][1]

        ### ALL COMBAT HAPPENS HERE \/
        correct_turn = 1 + math.ceil(turn_index / len(combatants))

        if current_combatant.allegiance == "Main Character":
            print("TURN " + str(correct_turn) + "#")
            modifiers = display_options(main_character, combatants, ally_modifiers)
            if modifiers:
                new_ally_modifiers, new_enemy_modifiers = modifiers
                ally_modifiers.append(new_ally_modifiers)
                enemy_modifiers.append(new_enemy_modifiers)

            # if new_modifiers:
            #     modifiers.append(new_modifiers)
        else:
            enemy_attack(current_combatant, combatants, enemy_modifiers)



        ### ALL COMBAT HAPPENS HERE /\
        check_and_remove_dead_enemies(combatants)

        turn_index += 1
        
    # AFTER COMBAT \/    
    print(combatants[0][1].name + " WAS VICTORIOUS!!!")
    victory = main_character.name == combatants[0][1].name
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
    for _ in combatants:
        char = _[1]
        if char.allegiance !="Main Character":
            print(str(char_index) + ".  " + char.name + "    HP: " + str(char.health))
            char_index += 1
    return input("\nEnter # of target you'd like to attack: ")

def item_options(main_character, combatants, modifiers):
    print_inventory(INVENTORY)
    item_target = int(input("\nEnter # of the item you'd like to use: ")) - 1
    item_to_use = INVENTORY[item_target]
    if item_to_use["type"] == "FOOD":
        main_character.gain_hp(item_to_use["hp"])
        remove_item(INVENTORY, item_target)
    return None

def attack_options(main_character, combatants, modifiers):
    target_index = int(targetting(main_character, combatants))
    target = None
    char_index = 1
    for _ in combatants:
        char = _[1]
        #print(char)
        if char.allegiance != "Main Character":
            if char_index == target_index:
                target = char
            char_index += 1
    
    #print_damage(main_character, target, main_character.base_damage)
    print("="*20)

    # modifies base damage
    base_damage = main_character.base_damage
    if modifiers:
        modified_damage = base_damage
        for modifier in modifiers:
            modified_damage = modifier(base_damage)
    else:
        modified_damage = base_damage

    # prints damage
    print(main_character.name + " did " + str(modified_damage) + " to " + target.name)
    print(target.name + " HP " + str(target.health) + " => " + str(target.health - modified_damage))
    target.health -= modified_damage

    # kills enemy and grants xp 
    if target.health <= 0:
        print(main_character.name + " defeated " + target.name)
        print(main_character.name + " gained " + str(target.exp_granted) + " XP!")
        main_character.gain_xp(target.exp_granted)

        # get loot
        if len(target.loot) > 0:
            random_drop = target.loot[random.randint(0, len(target.loot) - 1)] 
            add_item_to_inventory(INVENTORY, random_drop)

    # your character did X base damage to other character
    # your character did X additional damage to other character
    # other character hp 100 => 90
  
    return None

def enemy_attack(enemy, combatants, modifiers):
    valid_combatants = []
    for _ in combatants:
        char = _[1]
        #print(char)
        if char.allegiance is not enemy.allegiance:
            valid_combatants.append(char)
    
    target_index = random.randint(0, len(valid_combatants) - 1)
    target = valid_combatants[target_index]
    print("="*20)
    print(enemy.name + " did " + str(enemy.base_damage) + " to " + target.name)
    print(target.name + " HP " + str(target.health) + " => " + str(target.health - enemy.base_damage))
    target.health -= enemy.base_damage
  
    return None

def block_options(main_character, combatants, modifiers):
    # TODO DANNY HW
    return None

def ability_options(main_character, combatants, modifiers):
    main_character.print_skills()
    skill_target = int(input("\nEnter # of the skill you'd like to use: ")) - 1
    skill = main_character.skills[skill_target]
    return skill["function"]()

def escape_options(main_character, combatants, modifiers):
    return None

def display_options(main_character, combatants, modifiers):
    print("\n\nTurn options: ")
    print("1. Items")
    print("2. Attack")
    print("3. Block")
    print("4. Use Ability")
    print("5. Escape")
    player_choice = int(input("\nEnter what # move you'd like to make?")) - 1
    all_options = [item_options, attack_options, block_options, ability_options, item_options]
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