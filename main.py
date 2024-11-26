# Thayer Yang
# 25 NOV 2024
# Text Adeventure

# ----- IMPORTED MODULES -----
import time
from time import sleep as slp
import sys

# ----- CLASSES -----

class Player():

    def __init__(self):
        self.name = "No Name"
        self.health = 50
        self.max_health = 50
        self.inventory = []
        self.is_using = []

    def rename(self,name):
        self.name = name

    def showInfo(self):
        print(f"""Name: {self.name}
Health: {self.health}/{self.max_health}
Inventory = {self.inventory}""")
        
    def inInventory(self,item):
        if item in self.inventory:
            return True

# ----- FUNCTIONS -----

def type_print(str, delay=.01):
    for char in str:
        slp(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()

def display_list(list,delay=0):
    for index in range(len(list)):
        print(f"{index+1}: {list[index]}")
        slp(delay)
# ----- Variables -----

player = Player()
score = 0

duck_quacks = 0 # Used to see how many times the rubberduck is quacked

# ----- Name Input -----

name_decided = False

while not name_decided:
    name = input("What is your name?: ")
    ans = input(f"Is {name} correct? (y/n): ")

    if ans == 'y' or ans == "yes":
        player.rename(name)
        print()
        name_decided = True
    else:
        print("Well,")

# -----Starting Items-----
type_print(f"Hello Traveler {name}. Before you can embark your journey, you must select 3 items to begin.", .05)
slp(.5)

starting_items = ['hatchet', 'flint & steel', 'dagger', 'sandwich','tent','bandage','rubberduck']
print("Choose 3 items: ")

display_list(starting_items,.25)
print()

while len(player.inventory) < 3:
    
    try:
        choice = int(input("Choose an item by entering it's number: "))
        if choice <= len(starting_items) and choice >0:
            type_print(f"You picked up the {starting_items[choice-1]}!",.02)
            print()
            slp(1)

            player.inventory.append(starting_items[choice-1])
            starting_items.remove(starting_items[choice-1])
        else:
            print("Invalid Choice")
            slp(1)
            print()

    except ValueError:
        print("Please enter an integer.")
        print()

    if len(player.inventory) < 3:
        display_list(starting_items)

print(f"Lets see how you look so far!")
slp(.5)
print()
player.showInfo()
print()

type_print("Now you are ready to face the challenges ahead.", .05)

#-----ADVENTURE STARTS-----

type_print("You're eyes suddenly close because the sudden lights are too bright for you to look at..",.01)
slp(.2)
type_print("You see now that you have somehow ended up on the floor in the forest.",.02)
slp(2)
print("What will you do?")

scenario1 = True
s1_choices = ["Look around"]


while scenario1:

    if player.inInventory('tent'):
        s1_choices.append("Set up tent")
    if player.inInventory('flint & steel'):
        s1_choices.append("Attempt to start a fire")
    if player.inInventory("rubberduck"):
        s1_choices.append("Squeeze the rubberduck")

    display_list(s1_choices)

    try:
        choice = int(input("What will you do?: "))

        if (choice > 0 and choice <=len(s1_choices)):
            if s1_choices[choice] == s1_choices[0]:
                type_print("You see a village")
    
    except ValueError:
        print("Please enter an integer")

    



