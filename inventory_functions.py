from inventory_globals import *

# FUNCTIONS
def equip_item(items, player):
    print_inventory(items)
    item_number = min(int(input("\nWhich item number would you like to equip?\n")) - 1, len(INVENTORY) - 1)
    
    remove_item(items, item_number)

def add_item_to_inventory(items, new_item):
    potential_new_weight = calculate_weight(INVENTORY) + new_item["weight"] 
    if potential_new_weight <= MAX_WEIGHT:
        INVENTORY.append(new_item)
        print(new_item["name"] + " has been added to your inventory!")
    else:
        print("This item exceeds the weight limit!")

 
def print_inventory(items):
    print("\nItems in inventory:")
    for i in range(0, len(INVENTORY)):
        print(str(i + 1) + ". " + str(INVENTORY[i]["name"]))


def calculate_weight(items):
    total_weight = 0
    for i in INVENTORY:
        total_weight += i["weight"]
    return total_weight


def remove_item(items, item_number):
    item_to_be_deleted = items[item_number]
    del items[item_number]
    print(item_to_be_deleted["name"] + " has been removed")


def sell_item(items):
    print_inventory(items)
    item_number = min(int(input("\nWhich item number would you like to sell?\n")) - 1, len(INVENTORY) - 1)
    GOLD = GOLD + items[item_number]["buy price"] * SELL_PERCENTAGE
    
    remove_item(items, item_number)
    print("Total gold coins" + str(GOLD))