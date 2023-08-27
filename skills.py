from classes import * 

def first_strike():
    # Does MASSIVE damage (Only if used during the first turn)
    # takes more damage on the next turn(1.5/2)
    def increase_next_enemy_attack(base_damage):
        return base_damage * 2
    #       ally affect  ]]enemy affect
    return (None, increase_next_enemy_attack)

first_strike_skill = {"name" : "first_strike",
           "cost" : 80,
           "dot" : False,
           "damage" : 60,
           "incl_base": True,
           "level_scaling" : 0,
           "cooldown" : 1,
           "function" : first_strike,
           "ally_duration" : 1,
           "num_casts" : 1,
           "enemy_duration" : 1,
           "instant_cast" : True}

def parry():
    # negate incoming damage + stun
    # increase next attack damage slightly
    def increase_next_attack(base_damage):
        return base_damage + 10
    def block_next_enemy_attack(base_damage):
        return 0
    #       ally affect           enemy affect
    return (increase_next_attack, block_next_enemy_attack)

def burst_skill():
    return (None, None)

parry_skill = {"name" : "parry",
           "cost" : 10,
           "dot" : False,
           "cooldown" : 1,
           "function" : parry,
           "ally_duration" : 2,
           "enemy_duration" : 1,
           "instant_cast" : False}

burst_skill = {"name" : "burst",
           "cost" : 60,
            "dot" : False,
           "damage" : 7,
           "incl_base": False,
           "level_scaling" : 1.2,
           "cooldown" : 2,
           "function" : burst_skill,
           "num_casts" : 3,
           "instant_cast" : True}

def poison():
    # negate incoming damage + stun
    # increase next attack damage slightly
    # def block_next_enemy_attack(base_damage):
    #     return 0
    #       ally affect           enemy affect
    return (None, None)

tipped_arrow = {"name" : "tipped arrow",
           "cost" : 30,
           "damage" : 5,
           "dot" : True,
           "incl_base": True,
           "level_scaling" : 0.5,
           "cooldown" : 1,
           "function" : poison,
           "ally_duration" : 1,
           "num_casts" : 1,
           "enemy_duration" : 4,
           "instant_cast" : True}

double_attack_skill = {"name" : "double attack",
           "cost" : 30,
            "dot" : False,
           "damage" : 0,
           "incl_base": True,
           "level_scaling" : 1,
           "cooldown" : 2,
           "function" : burst_skill,
           "num_casts" : 2,
           "instant_cast" : True}