from items import *

class base_enemy:
    def __init__(self):
        self.allegiance = "enemy"
        self.base_damage = 10
        self.health = 50 
        self.max_health = 50
        self.max_energy = 50
        self.energy = 50 
        self.skills = [] 
        self.speed = 10
        self.defense = 1
        self.name = ""
        self.loot = []
        self.gold = 0
        self.statuses = []
        self.level = 0
    
    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))        
        print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))

    def level_up(self):
        self.defense += 1
        self.max_health *= 1.1
        self.base_damage *= 1.1
        self.level += 1

    def __str__(self):
        return "Lvl. " + str(self.level) + " " + self.name

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

class Faye_Soldier(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 10
        self.allegiance = "Faye, Main Character"
        self.name = "Guardian"
        self.skills = ["None"]
        self.speed = 8
        self.health = 100
        self.max_health = 100
        self.exp_granted = 20

class Yeti(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 15
        self.allegiance = "None"
        self.name = "Yeti"
        self.speed = 9
        self.health = 200
        self.max_health = 200
        self.exp_granted = 250

class Unknown_1(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 1000
        self.allegiance = "None"
        self.name = "0"
        self.skills = ["None"]
        self.speed = 8
        self.health = 90
        self.max_health = 90
        self.exp_granted = 1000
        
class Trap_1(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 50
        self.allegiance = "Traps"
        self.name = "Bear Trap"
        self.speed = 100
        self.health = 1
        self.max_health = 1
        self.exp_granted = 0
        
class Red_Dragon(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 20
        self.allegiance = "Dragons"
        self.name = "Jeldruss, Lord of the Red"
        self.skills = ["Scorched Earth"]
        self.speed = 25
        self.health = 250
        self.max_health = 250
        self.exp_granted = 500
        
class Eagle(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 15
        self.allegiance = "None"
        self.name = "Eagle"
        self.skills = ["Dive Up"]
        self.speed = 17
        self.health = 40
        self.max_health = 40
        self.exp_granted = 30
        
class XP(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 0
        self.allegiance = "None"
        self.name = "Dummy"
        self.skills = [""]
        self.speed = 0
        self.health = 10
        self.max_health = 10
        self.exp_granted = 100000000

class Giant(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 5
        self.allegiance = "None"
        self.name = "Giant"
        self.skills = ["Shockwave"]
        self.speed = 2
        self.health = 200
        self.max_health = 200
        self.exp_granted = 300
        

class Trap_9000(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 1000000
        self.allegiance = "Traps"
        self.name = "Ultimate Trap"
        self.speed = 100000
        self.health = 1
        self.max_health = 1
        self.exp_granted = 0
        
class Enemy_Scout(base_enemy):
    def __init__(self):
        super().__init__()
        self.base_damage = 15
        self.allegiance = "None"
        self.name = "Turp's Scout"
        self.skills = ["Last Stand"]
        self.speed = 12
        self.health = 100
        self.max_health = 100
        self.exp_granted = 120
        

        
