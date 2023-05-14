from classes import * 

def parry():
    # negate incoming damage + stun
    # increase next attack damage slightly
    def increase_next_attack(base_damage):
        return base_damage + 10
    def block_next_enemy_attack(base_damage):
        return 0
    return (increase_next_attack, block_next_enemy_attack)

parry_skill = {"name" : "parry",
           "cost" : 10,
           "cooldown" : 1,
           "function": parry}