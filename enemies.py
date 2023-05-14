from items import *

class base_enemy:
    def __init__(self):
        self.allegiance = "enemy"
        self.base_damage = 10
        self.health = 50 
        self.max_health = 50
        self.skills = [] 
        self.speed = 10
        self.defense = 1
        self.name = ""
        self.loot = []
        self.gold = 0
    
    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))        
        print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))

class Wolf(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 15
        self.allegiance = "Wolfs"
        self.name = "Grey Wolf"
        self.skills = ["bite"]
        self.speed = 15
        self.health = 50
        self.max_health = 50
        self.exp_granted = 80
        self.loot = [wolf_meat]

class Bear(base_enemy):
    def __init__(self):
        super().__init__()
        self.allegiance = "Bears"
        self.name = "Grizzly Bear"
        self.skills = ["trample"]
        self.speed = 12
        self.base_damage = 20
        self.health = 150
        self.max_health = 150
        self.defense = 3
        self.exp_granted = 100
        self.loot = [bear_meat]


class Bandit(base_enemy):
    def __init__(self):
        super().__init__()
        self.allegiance = "Thieves Guild"
        self.name = "Sloppy bandit"
        self.skills = ["mug"]
        self.speed = 11
        self.base_damage = 8
        self.health = 60
        self.max_health = 60
        self.defense = 3
        self.exp_granted = 40
        self.gold = 50
        self.loot = [dagger_0]
        
class Assassin(base_enemy):
    def __init__(self):
        super().__init__()
        self.allegiance = "Assassin's Guild"
        self.name = "Trained Assassin"
        self.skills = ["double attack"]
        self.speed = 13
        self.base_damage = 40
        self.health =30
        self.max_health = 30
        self.defense = 2
        self.exp_granted = 75
        self.gold = 25
        self.loot = [dagger_1]
        