import skills 
from inventory import * 

class base_class:
    def __init__(self):
        self.current_level = 1
        self.level_increase_factor = 1.15
        self.xp_to_next_level = 100
        self.current_xp = 0
        self.max_energy = 100
        self.energy = 100
        self.weapon = None
        self.shield = None
        self.helemt = None
        self.breastplate = None
        self.greaves = None
        self.leggings = None
        self.bonus_damage = 0
        self.bonus_defense = 0

    def get_weapon(self):
        if self.weapon: return self.weapon["name"] 
        return None
    
    def get_shield(self):
        if self.shield: return self.shield["name"] 
        return None

    def get_helmet(self):
        if self.helemt: return self.helemt["name"] 
        return None

    def get_breastplate(self):
        if self.breastplate: return self.breastplate["name"] 
        return None

    def get_greaves(self):
        if self.greaves: return self.greaves["name"] 
        return None

    def get_helmet(self):
        if self.helemt: return self.helemt["name"] 
        return None

    def get_leggings(self):
        if self.leggings: return self.leggings["name"] 
        return None

    def print_gear(self):
        print("Items equipped:")
        print("Weapon: " + str(self.get_weapon()))
        print("shield: " + str(self.get_shield()))
        print("helemt: " + str(self.get_helmet()))
        print("breastplate: " + str(self.get_breastplate()))
        print("greaves: " + str(self.get_greaves()))
        print("leggings: " + str(self.get_leggings()))

    def calc_bonus_damage(self):
        return self.weapon["damage"]

    def calc_bonus_defense(self):
        bonus_defense = 0

    def change_energy(self, amount):
        energy_before = self.energy
        self.energy += amount
        if self.energy >= self.max_energy:
            self.energy = self.max_energy
        if self.energy < 0:
            self.energy = 0
        energy_after = self.energy
        energy_diff = energy_after - energy_before
        print("Regained " + str(energy_diff) + " Energy")
        

    
    def equip_item(self, item, inventory):
        if item["type"] == "HELMET":
            if self.helmet: 
                add_item_to_inventory(inventory, self.helmet)
            self.helmet = item
        if item["type"] == "SHIELD":
            if self.shield: 
                add_item_to_inventory(inventory, self.shield)
            self.shield = item
        if item["type"] == "WEAPON":
            if self.weapon: 
                add_item_to_inventory(inventory, self.weapon)
            self.weapon = item
        if item["type"] == "BREASTPLATE":
            if self.breastplate: 
                add_item_to_inventory(inventory, self.breastplate)
            self.breastplate = item
        if item["type"] == "GREAVES":
            if self.greaves: 
                add_item_to_inventory(inventory, self.greaves)
            self.greaves = item
        if item["type"] == "LEGGINGS":
            if self.leggings: 
                add_item_to_inventory(inventory, self.leggings)  
            self.leggings = item
        self.bonus_damage = self.calc_bonus_damage()      


    def calc_xp_to_next_level(self):
       self.xp_to_next_level *= self.level_increase_factor 
       self.xp_to_next_level = int(self.xp_to_next_level)


    def gain_xp(self, xp):
        self.current_xp += xp
        if self.current_xp >= self.xp_to_next_level:
            self.current_level += 1
            print("You leveled up to " + str(self.current_level) + "!")
            remaining_xp = self.current_xp - self.xp_to_next_level
            self.current_xp = 0
            self.calc_xp_to_next_level()
            self.level_up()
            self.gain_xp(remaining_xp)

            

    def level_up(self):
        self.max_health += 5 
        self.base_damage += 2
        self.health = self.max_health
        self.max_energy += 5
        self.energy = self.max_energy

    def gain_hp(self, hp_amount):
        hp_before = self.health
        self.health += hp_amount
        if self.health > self.max_health: 
            self.health = self.max_health
        hp_after = self.health
        hp_diff = hp_after - hp_before
        print("Regained " + str(hp_diff) + " HP")

    def print_skills(self):
        print("\n\nYour skills are: ")
        skill_index = 1
        for skill in self.skills:
            print(str(skill_index) + ".  " + str(skill))
            skill_index += 1



class Scout(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 20
        self.max_health = 90 
        self.health = 90
        self.max_energy = 120
        self.energy = 120
        self.skills = [skills.first_strike_skill]
        self.speed = 15
        self.defense = 0

    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))    
        print("Energy: " + str(self.energy))      
        #print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))
        print("Special Ability: First Strike")

class Fighter(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 15
        self.max_health = 110 
        self.health = 110
        self.max_energy = 90
        self.energy = 90
        self.skills = [skills.parry_skill] 
        self.speed = 9
        self.defense = 0
    
    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))
        print("Energy: " + str(self.energy))    
        #print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))
        print("Special Ability: Parry")



class ApprenticeMage(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 17
        self.max_health = 100
        self.health = 100
        self.max_energy = 150
        self.energy = 150
        self.skills = [skills.burst_skill] 
        self.speed = 10
        self.defense = 0
        
    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))
        print("Energy: " + str(self.energy))         
        #print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))
        print("Special Ability: Burst")



class Archer(base_class):
    def __init__(self):
        super().__init__()
        self.allegiance = "Main Character"
        self.name = "Main Character"
        self.base_damage = 15
        self.max_health = 90
        self.health = 90
        self.max_energy = 100
        self.energy = 100
        self.skills = [skills.tipped_arrow]
        self.speed = 12
        self.defense = 0

    def print_stats(self):
        print("Base damage: " + str(self.base_damage))
        print("Health: " + str(self.health))
        print("Energy: " + str(self.energy))      
        #print("Special skill: " + self.special_skill)
        print("Speed: " + str(self.speed))
        print("Defense: " + str(self.defense))
        print("Special Ability: Tipped Arrow")