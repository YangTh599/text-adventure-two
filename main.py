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

    def rename(self,name):
        self.name = name

    def showInfo(self):
        print(f"""Name: {self.name}
Health: {self.health}/{self.max_health}
Inventory = {self.inventory}""")

# ----- FUNCTIONS -----

def type_print(str, delay):
    for char in str:
        slp(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()

# ----- Variables -----

player = Player()
score = 0
backpack = []

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

starting_items = ['hatchet', 'flint & steel', 'dagger', 'sandwich','tent','bandage']
print("Choose 3 items: ")

for i in range(len(starting_items)):
    print(f"{i+1}: {starting_items[i]}")
    slp(.75)
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
        for i in range(len(starting_items)):
                print(f"{i+1}: {starting_items[i]}")

print(f"Lets see how you look so far!")
slp(.5)
print()
player.showInfo()
print()

type_print("Now you are ready to face the challenges ahead.", .05)




