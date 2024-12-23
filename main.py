# Thayer Yang
# 25 NOV 2024
# Text Adeventure

# ----- IMPORTED MODULES -----
import time
from time import sleep as slp
from random import randint
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
            if self.isUsing(item): #Checks if item is in inventory
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
    
    def checkQuacks(self):
        if self.duck_quacks <=1:
            print(f"You have squeezed the duck {self.duck_quacks} times")
        else:
            print(f"You have squeezed the duck {self.duck_quacks} times")

# class Enemy():

#     def __init__(self)


            

# ----- FUNCTIONS -----

def type_print(str, delay=.05,next_line=True):
    for char in str:
        slp(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    if next_line:
        sys.stdout.write("\n")
    sys.stdout.flush()

def display_list(list,delay=0):
    for index in range(len(list)):
        print(f"{index+1}: {list[index]}")
        slp(delay)

def rng(die=6,roll_needed=3,num_specific=False):
    roll = randint(1,die+1)
    if not num_specific:
        if roll >= roll_needed:
            return True
        else:
            return False
    else:
        if roll == roll_needed:
            return True
        else:
            return False

def list_check(list,element):
    if element in list:
        return True
    else:
        return False


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
            name_decided = True
        else:
            player.rename(name)
            print()
            name_decided = True
    else:
        print("Well,")

# -----Starting Items-----
type_print(f"Hello Traveler {player.name}. Before you can embark your journey, you must select 3 items to begin.")
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
    if player.inInventory('tent') and not list_check(s1_choices,"Set up tent"):
        s1_choices.append("Set up tent") # Priority Index 1
    if (player.inInventory('flint & steel') or player.inInventory('firewood')) and not list_check(s1_choices,"Attempt to start a fire"):
        s1_choices.append("Attempt to start a fire") # Priority Index 2
    if player.inInventory("rubberduck") and not list_check(s1_choices,"Squeeze the rubberduck"):
        s1_choices.append("Squeeze the rubberduck") # Priority is Last Index

    display_list(s1_choices)

    try:
        choice = int(input("What will you do?: "))
        choice -=1

        if s1_choices[choice] == "Look around":

            type_print("You see a village not too far..")
            slp(.2)
            type_print("You estimate a 10 minute walk to the village.")
            slp(.2)
            type_print("You also see that there are a bunch of sticks and leaves on the ground.")
            slp(1.5)

            s1_choices.insert(0,"Walk to the village")
            s1_choices.insert(1,"Gather firewood")
            s1_choices.remove("Look around")

        elif s1_choices[choice] == "Walk to the village":
            type_print("You walk to the village.")
            slp(.5)
            type_print("It take you 10 minutes..")
            slp(.5)
            type_print("You get to a bridge before the village entrance..")
            slp(.5)
            type_print("You cross the bridge and then, ", next_line=False)
            slp(.75)
            type_print("the bridge collapses behind you..")
            slp(1)

            if player.isUsing("tent"):
                type_print("You realized you've forgotten your tent!")
                type_print("You no longer have a tent")
                player.is_using.remove("tent")
                slp(1)
            
            slp(1)
            scenario1 = False
            
        
        elif s1_choices[choice] == "Set up tent":
            type_print("You spent 5 minutes setting up the tent..")
            slp(1)
            player.useItem('tent')
            type_print("Your tent is now set up")

            index = s1_choices.index("Set up tent")
            s1_choices.insert(index,"Pack up tent")
            s1_choices.remove("Set up tent")

        elif s1_choices[choice] == "Pack up tent":
            type_print("You spend 4 minutes packing up the tent..")
            slp(.8)
            player.useItem('tent',True)
            type_print("Your tent is now packed up")

            index = s1_choices.index("Pack up tent")
            s1_choices.insert(index,"Set up tent")
            s1_choices.remove("Pack up tent")

        elif s1_choices[choice] == "Gather firewood":
            type_print("You look down at your feet.")
            slp(.5)
            if rng():
                type_print("Some firewood seem to be magically placed between your legs..")
                player.inventory.append("firewood")
                slp(1)
                print("You now got firewood!")

                s1_choices.remove("Gather firewood")
            else:
                if "hatchet" in player.inventory:
                    type_print("You remember you have a hatchet with you.")
                    slp(.2)
                    type_print("You spent 10 minutes gathering firewood")
                    player.inventory.append("firewood")
                    slp(1)
                    print("You now got firewood!")

                    s1_choices.remove("Gather firewood")
                else:
                    type_print("You try to look for good firewood")
                    type_print("You see a lot of small sticks but nothing good..")
                    type_print("You will not be able to start a fire yet.")
                    slp(1)
            if not "Attempt to start a fire" in s1_choices:
                s1_choices.insert(len(s1_choices)-1,"Attempt to start a fire")


        elif s1_choices[choice] == "Attempt to start a fire":

            if player.inInventory("firewood"):
                type_print("You set up the fire wood")
                slp(1.2)

                if player.inInventory("flint & steel"):
                    type_print("You spark a fire onto the firewood.")
                    slp(.5)
                    print("You now have an ongoing fire.")

                    player.useItem("firewood")
                    s1_choices.remove("Attempt to start fire")
                else:    
                    type_print("You stare at the firewood..")
                    slp(.5)
                    print("Nothing happened to the firewood..")
                    slp(.5)
                    type_print("You picked the firewood back up")
            else:
                type_print("You spark the ground...")
                slp(1.2)
                print("It did nothing")

        elif s1_choices[choice] == "Squeeze the rubberduck":
            if player.inInventory("rubberduck"):
                if rng(100,92,True):
                    type_print("THE DUCK EXPLODED",.02)
                    slp(2)

                    dmg = randint(45,50)
                    type_print(f"You took {dmg} damage. ",next_line=False)
                    player.health -= dmg
                    type_print(f"You now have {player.health}/{player.max_health} health.")

                    player.inventory.append("broken rubberduck")
                    player.inventory.remove("rubberduck")
                else:
                    type_print("The duck quacked happily")
                    player.duck_quacks +=1
                    player.checkQuacks()
            elif player.inInventory("broken rubberduck"):
                type_print("You tried to squeeze the rubberduck..")
                slp(1)
                type_print("Nothing came out..")
                slp(1)

        print()

    
    except IndexError:
        if len(s1_choices) ==1:
            type_print("...",1)
            print("Enter the first integer")
        else:
            print(f"Please enter an integer between 1 and {len(s1_choices)}")
    except ValueError:
        print("Please enter an integer")


print()
slp(1)
print("You made it to the village!")
type_print("Let's see how you're doing.")
slp(1)
player.showInfo()




