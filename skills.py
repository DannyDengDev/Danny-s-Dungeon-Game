from classes import * 

# def first_strike():
#     # Does MASSIVE damage (Only if used during the first turn)
#     # takes more damage or lower health for the next turn greatly
#     def increase_next_attack(base_damage):
#         return base_damage + 10
#     def block_next_enemy_attack(base_damage):
#         return 0
#     #       ally affect           ]]enemy affect
#     return (increase_next_attack, block_next_enemy_attack)

# parry_skill = {"name" : "parry",
#            "cost" : 10,
#            "cooldown" : 1,
#            "function": parry}

def parry():
    # negate incoming damage + stun
    # increase next attack damage slightly
    def increase_next_attack(base_damage):
        return base_damage + 10
    def block_next_enemy_attack(base_damage):
        return 0
    #       ally affect           enemy affect
    return (increase_next_attack, block_next_enemy_attack)

parry_skill = {"name" : "parry",
           "cost" : 10,
           "cooldown" : 1,
           "function" : parry,
           "ally_duration" : 2,
           "enemy_duration" : 1,
           "instant_cast" : False}

def burst():
    return (None, None)

burst_skill = {"name" : "burst",
           "cost" : 60,
           "damage" : 18,
           "level_scaling" : 1.1,
           "cooldown" : 2,
           "function": burst,
           "instant_cast" : True}

# def tipped_arrow():
#     # 5 Poison damage
#     def poison(base_damage):
#         return base_damage + 10
#     #       ally affect           enemy affect
#     return (poison, block_next_enemy_attack)

# burst_skill = {"name" : "burst",
#            "cost" : 15,
#            "cooldown" : 2,
#            "function": poison,
#            "duration": 3}