from enemies import *

class StartTown:
    def __init__(self):
        self.name = "Faye Town"
        self.villagers = []
        self.merchants = []
        self.guards = [Faye_Soldier()]
        self.enemies = [XP()]
        self.night_enemies = [XP()]
        self.description = "Peaceful village with a lively town center. A safe town patrolled by guards but with few merchants."
        self.connecting_locations = [Grasslands]

# group of theives
class Grasslands:
    def __init__(self):
        self.name = "Faye Fields"
        self.villagers = []
        self.merchants = []
        self.guards = [Faye_Soldier()]
        self.enemies = [Bandit()]
        self.night_enemies = [Bandit()]
        self.description = "Wide fields of grass with plenty of wildlife and few bandits."
        self.connecting_locations = [StartTown, Forest, Mountain_Range]

# rabbit with rabbies, screaming witch
class Forest:
    def __init__(self):
        self.name = "Farther Forest"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Wolf(), Trap_1()]
        self.night_enemies = [Wolf(), Trap_1()]
        self.description = "Towering trees covered with foliage hiding more dangerous wildlife."
        self.connecting_locations = [Grasslands, Mountain_Range, Desert, Sea]

# golem, giant eagle
class Mountain_Range:
    def __init__(self):
        self.name = "Jagged Cliffs"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Bear()]
        self.night_enemies = [Bear(), Trap_1()]
        self.description = "A treacherous mountain range with bears that have awoken from slumber, and seeks food."
        self.connecting_locations = [Grasslands, Forest, Snowy_Mountain, Desert]


# frost dragon, undead skeleton, necromancer
class Snowy_Mountain:
    def __init__(self):
        self.name = "Frosty Peaks"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Yeti()]
        self.night_enemies = [Yeti()]
        self.description = "Something hides in the snow"
        self.connecting_locations = [Mountain_Range]

# scorpion, giant scorpion
class Desert:
    def __init__(self):
        self.name = "Scorched Desert"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Red_Dragon()]
        self.night_enemies = [Enemy_Scout]
        self.description = "This buring area once used to be lush grassland"
        self.connecting_locations = [Forest, Mountain_Range, Sea, Oasis, Hostile_Plains]

class Oasis:
    def __init__(self):
        self.name = "Flourishing Oasis"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = []
        self.night_enemies = []
        self.description = "An area where even the heat of the sun can't defeat"
        self.connecting_locations = [Desert]


# kraken, serpent, pirate, pirate king
class Sea:
    def __init__(self):
        self.name = "The Grim Sea"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = []
        self.night_enemies = []
        self.description = "A beautiful sea"
        self.connecting_locations = [Forest, Desert]

class Hostile_Plains:
    def __init__(self):
        self.name = "Perilous Plains"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Giant()]
        self.night_enemies = [Assassin()]
        self.description = "A dangerous area that holds multiple hostiles"
        self.connecting_locations = [Mountain_Range, Desert]
        
#all_locations = [StartTown, Grasslands, Forest]

# Grasslands      # type object
#                 # \/
# Grasslands()    # actual object