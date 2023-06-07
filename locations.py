from enemies import *

class StartTown:
    def __init__(self):
        self.name = "Faye Town"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Protector(), Guardian()]
        self.description = "Peaceful village with a lively town center. A safe town patrolled by guards but with few merchants."
        self.connecting_locations = [Grasslands]


class Grasslands:
    def __init__(self):
        self.name = "Faye Fields"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Bandit()]
        self.description = "Wide fields of grass with plenty of wildlife and few bandits."
        self.connecting_locations = [StartTown, Forest, Mountain_Range]

class Forest:
    def __init__(self):
        self.name = "Farther Forest"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Wolf()]
        self.description = "Towering trees covered with foliage hiding more dangerous wildlife."
        self.connecting_locations = [Grasslands, Mountain_Range, Desert, Sea]

class Mountain_Range:
    def __init__(self):
        self.name = "Jagged Cliffs"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Bear(), Assassin()]
        self.description = "A treacherous mountain range with bears that have awoken from slumber, and seeks food."
        self.connecting_locations = [Grasslands, Forest, Snowy_Mountain, Desert]
    
class Snowy_Mountain:
    def __init__(self):
        self.name = "Frosty Peaks"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Yeti]
        self.description = "Something lurks in the snow"
        self.connecting_locations = [Mountain_Range]

class Desert:
    def __init__(self):
        self.name = "Scorched Desert"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Yeti]
        self.description = "This buring area once used to be lush grassland"
        self.connecting_locations = [Forest, Mountain_Range, Sea]
        
class Sea:
    def __init__(self):
        self.name = "The Grim Sea"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Yeti]
        self.description = "A beautiful sea"
        self.connecting_locations = [Forest, Desert]
        
#all_locations = [StartTown, Grasslands, Forest]

# Grasslands      # type object
#                 # \/
# Grasslands()    # actual object