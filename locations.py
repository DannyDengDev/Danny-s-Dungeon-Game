from enemies import *

class StartTown:
    def __init__(self):
        self.name = "Faye Town"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = []
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
        self.connecting_locations = [StartTown, Forest]

class Forest:
    def __init__(self):
        self.name = "Farther Forest"
        self.villagers = []
        self.merchants = []
        self.guards = []
        self.enemies = [Bear(), Wolf()]
        self.description = "Towering trees covered with foliage hiding more dangerous wildlife."
        self.connecting_locations = [Grasslands]

#all_locations = [StartTown, Grasslands, Forest]

# Grasslands      # type object
#                 # \/
# Grasslands()    # actual object