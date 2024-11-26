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
        self.duck_quacks = 0 # Used to see how many times the rubberduck is quacked


    def rename(self,name): #Renames the player
        self.name = name

    def showInfo(self):
        print(f"""Name: {self.name}
Health: {self.health}/{self.max_health}
Inventory = {self.inventory}""")
        
    def inInventory(self,item):
        """Checks if an item is in the player's inventory"""

        if item in self.inventory:
            return True
        else:
            return False
        
    def isUsing(self,item):
        """Checks if player is using something from thier inventory"""

        if item in self.is_using:
            return True
        else:
            return False
        
    def useItem(self,item, put_back=False):
        #Moves item from inventory to using
        if put_back:
            if self.inUsing(item): #Checks if item is in inventory
                index = self.is_using.index(item)

                self.inventory.append(self.is_using[index])
                self.is_using.remove(self.is_using[index])
        
        else:
            if self.inInventory(item): #Checks if item is in inventory
                index = self.inventory.index(item)

                self.is_using.append(self.inventory[index])
                self.inventory.remove(self.inventory[index])
            else:
                print(f"You can't {item}")

            

# ----- FUNCTIONS -----

def type_print(str, delay=.05):
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

# ----- Name Input -----

name_decided = False

while not name_decided:
    name = input("What is your name?: ")
    if name == "":
        ans = input("You have not entered a name. Are you sure you don't want to enter a name? (y/n): ")
    else:
        ans = input(f"Is {name} correct? (y/n): ")

    if ans == 'y' or ans == "yes":
        if name == "":
            type_print("If you insist on that, you should just be called \"Alyx\"")
            player.rename("Alyx")
        else:
            player.rename(name)
            print()
            name_decided = True
    else:
        print("Well,")

# -----Starting Items-----
type_print(f"Hello Traveler {name}. Before you can embark your journey, you must select 3 items to begin.")
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

type_print("Now you are ready to face the challenges ahead.")

#-----ADVENTURE STARTS-----

type_print("You're eyes suddenly close because the sudden lights are too bright for you to look at..")
slp(.2)
type_print("You see now that you have somehow ended up on the floor in the forest.")
slp(2)
print("What will you do?")

scenario1 = True
s1_choices = ["Look around"] #Look around at Index 0


while scenario1:

    # --Additional Choices--
    if player.inInventory('tent'):
        s1_choices.append("Set up tent") # Priority Index 1
    elif player.isUsing('tent'):
        s1_choices.append("Pack up tent")
    if player.inInventory('flint & steel'):
        s1_choices.append("Attempt to start a fire") # Priority Index 2
    if player.inInventory("rubberduck"):
        s1_choices.append("Squeeze the rubberduck") # Priority is Last Index

    display_list(s1_choices)

    try:
        choice = int(input("What will you do?: "))

        if s1_choices[choice] == "Look around":
            type_print("You see a village not too far..")
            slp(.2)
            type_print("You estimate a 10 minute walk to the village.")
            slp(1)

            s1_choices.remove("Look around")
            s1_choices.insert(0,"Walk to the village")

        elif s1_choices[choice] == "Set up tent":
            type_print("You spent 5 minutes setting up the tent..")
            slp(1)
            player.useItem('tent')
            type_print("Your tent is now set up")

        elif s1_choices[choice] == "Pack up tent":
            type_print("You spend 4 minutes packing up the tent..")
            slp(.8)
            player.useItem('tent',True)
            type_print("Your tent is now packed up")            




    except IndexError:
        if len(s1_choices) ==1:
            type_print("...",1)
            print("Enter the first integer")
        else:
            print(f"Please enter an integer between 1 and {len(s1_choices)}")
    except ValueError:
        print("Please enter an integer")

    



