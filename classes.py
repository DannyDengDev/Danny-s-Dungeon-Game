class base_class:
    def __init__(self):
        self.current_level = 1
        self.level_increase_factor = 1.2
        self.xp_to_next_level = 100
        self.current_xp = 0
        self.weapon = None
        self.shield = None
        self.helemt = None
        self.breastplate = None
        self.greaves = None
        self.leggings = None
        self.bonus_damage = 0
        self.bonus_defense = 0

    def calc_bonus_damage(self):
        self.bonus_damage = self.weapon.damage

    # def calc_bonus_defense(self):
    #     self.bonus_defense = sum([x])

    
    def equip_item(self, item):
        if item.type == "HELMET":
            self.helmet = item
        if item.type == "SHIELD":
            self.shield = item
        if item.type == "WEAPON":
            self.weapon = item
        if item.type == "BREASTPLATE":
            self.breastplate = item
        if item.type == "GREAVES":
            self.greaves = item
        if item.type == "LEGGINGS":  
            self.leggings = item      


    def calc_xp_to_next_level(self):
       self.xp_to_next_level *= self.level_increase_factor 
       self.xp_to_next_level = int(self.xp_to_next_level)


    def gain_xp(self, xp):
        self.current_xp += xp
        if self.current_xp >= self.xp_to_next_level:
            self.current_level += 1
            print("You leveled up to " + str(self.current_level) + "!")
            remaining_xp = self.current_xp - self.xp_to_next_level
            self.current_xp = remaining_xp
            self.calc_xp_to_next_level()
            self.level_up()

    def level_up(self):
        self.max_health += 5 
        self.base_damage += 2
        self.health = self.max_health




class Scout(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 20
        self.max_health = 80 
        self.health = 80
        self.special_skill = "observe" 
        self.speed = 15
        self.defense = 0

    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))        
        print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))

class Fighter(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 15
        self.max_health = 110 
        self.health = 110
        self.special_skill = "parry" 
        self.speed = 9
        self.defense = 0
    
    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))        
        print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))



class ApprenticeMage(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 17
        self.max_health = 100
        self.health = 100
        self.special_skill = "burst" 
        self.speed = 10
        self.defense = 0
        
    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))        
        print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))



class Archer(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 15
        self.max_health = 90
        self.health = 90
        self.special_skill = "true shot" 
        self.speed = 12
        self.defense = 0

    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))        
        print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))