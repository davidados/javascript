import time
import sys
import random

item = ""
equipped_item = ""
items = ["key", "ticket"]



def print_pause(message):
    print(message)
    time.sleep(2)

def game_over():
    print("game is over")

def intro():
    print_pause("It's summer, the temperature is unbearable, \n"
                "there is no air conditioner in your flat.")
    print_pause("The internet has gone, some COVID rules are still in effect." )
    print_pause("Furthermore, it's TW week, so you deciced to visit Coodcool's headquarter phisically.")
    print_pause("This is how an epic journey started.")

     
def location_flat():
    print_pause("It's morning, you already showered and dressed up for the departure, \n
    "although you dont find your keys." )
    print_pause("What do you do?
    print_pause("A.) Lay back, and tell Coodcool that you are sick.")
    print_pause("B.) Start looking for your keys")
    print_pause("Please press A or B")
    #input here
    print_pause("Where would you look for it?") 
    print_pause("A.) Desk.")
    print_pause("B.) Bed")
    print_pause("C.) Drawer")
    print_pause("D.) Holder")
    #input here









intro()