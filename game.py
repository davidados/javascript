import time
import sys
import random

item = ""



def print_pause(message):
    print(message)
    time.sleep(2)

def game_over():
    print("game is over, you lost")

def game_finished():
    print_pause("You succesfully reached your destination, now you can be cool in Codecool.")

def intro():
    print_pause("It's summer, the temperature is unbearable, \n"
                "there is no air conditioner in your flat.")
    print_pause("The internet has gone, some COVID rules are still in effect." )
    print_pause("Furthermore, it's TW week, so you deciced to visit Codecool's headquarter phisically.")
    print_pause("This is how an epic journey started.")

     

def location_flat():
    print_pause("It's morning, you already showered and dressed up for the departure,")
    print_pause("although you dont find your keys.")
    print_pause("What do you do?")
    print_pause("1.) Lay back, and tell Codecool that you are sick.")
    print_pause("2.) Start looking for your keys")
    print_pause("Please press \"1\" or \"2\"")
    response_flat()
    print_pause("Where would you look for it?") 
    print_pause("1.) Desk.")
    print_pause("2.) Bed")
    print_pause("3.) Drawer")
    print_pause("4.) Holder")
    response_flat2()


def response_flat():
    response = input()
    if response == "1":
        print_pause("You told Codecool that you are sick, you still feel hot, and with no internet, you wasted a day of your life. :(")
        game_over()
    elif response == "2":
        print_pause("I knew you wouldn't give up this easy.")
    else:
        response_flat()

def response_flat2():
    key_location = random.randint(1, 4)
    response = input()
    if key_location == int(response):
        print_pause("You have found your keys")
        item.append("keys")
        else:
                print("There is no key")
        else:
            room1_response()
   



def location_bus_stop():
    print_pause("Now that you have your keys, you can head to CodeCool.")
    print_pause("On your way to to bus stop you relaize that you don't have travel pass nor face mask.")
    print_pause("But your attention suddely shifts to a busker across the street,  the tone feels similar to you.")
    print_pause("You see that there is some case in his basket")
    print_pause("What do you do?")
    print_pause("1.) Try to take some cash")
    print_pause("2.) Just enjoy the music for a couple of moments.")
    print_pause("3.) Continue your journey to the bus stop.")
    response_bus_stop1()
    print_pause("You see that the bus is coming fast, you start run for it, you catch it.")
    print_pause("If you have some cash, you can buy ticket from the driver, otherwise you risk it to get caught by the ticket inspector.")
    print_pause("What is your next step?")
    print_pause("1.) You change your mind and won't step into the bus.")

    print_pause("2.) Risk it to travel without ticket.")
    #Random észreveszi vagy nem
    print_pause("3.) Buy ticket from the driver")
    response_bus_stop2()

def commit_crime():
    crime_chances = random.randint(1, 2)
        if crime_chances == "1":
            print_pause("You succesfully get away with this sin.")
        else:
            print_pause("You got caught!")
            game_over()
            quit()


def response_bus_stop1():
    response = input()
    if response == "1":
        commit_crime()
        item.append("cash")
    elif response == "2":
        print_pause("You know what is this right? Gyongyhaju lany...")
    elif response == "3":
        print_pause("You are really determined!")
    else:
        response_bus_stop1()

def response_bus_stop2():
    if response == "1":
        print_pause("You should have had give up now, you were doing great!")
        game_over()


def location_codecool():
    print_pause("You successfully arrived to Codecool's headquarter, but due to the absent of your mask the receptionist can't let you pass.")
    print_pause("Now what to do?")
    print_pause("1.) Check the bin for possible used masks.")
    print_pause("2.) Head back to home.")
    #game_over(),
    print_pause("3.) You don't care what does the receptionist says, you just go on straight.")
    #input here
# A response: Találtál egy maszkot a kuka mögött
# B response: Nem mehetsz haza, megsülsz az utcán, olyan meleg van
# C response: A portás megelégelte a renitenskedést, és kiraktad a szűröd game_over()
#Van maszk az inventoryban, tovább mehetsz az irodába

def location_office():
    print_pause("You stand in front of the door to your class,")
    print_pause("but you just remember that you also need Nold Account,")
    print_pause("what you obviously don't have.")
    print_pause("When you try to enter, \"Spirit of Every Nold Account\" appears.")
    print_pause("SoENA: \"If you can answer for my three riddles, you shall enter the school, or may fall, and you can't enter on your own ever again, only by letting in by others.\"")
    print_pause("Question 1.) How much \"%\" can you miss from the attendance?")
    #input here
    print_pause("Question 2.) After the summer vacation, how many times should you attend to school in \"TW\" and in \"SI\" week?")
    #input here
    print_pause("Question 3.) Does it worth to take Consulatation? \"yes\" or \"no\"")
    #input here
    # Ha rossz valamelyik válasz, akkor:
    # Nem kaphatsz soha többé Nold accountot. Eleinte nem érzékeled még a probléma súlyosságát, csak mikor csöngetsz, és kiderül, hogy a pandémia miatt senki sincsen az officeban, hogy az ajtón beengedjen. Egyedül maradtál, és lekésted az attendancet. Game_over




def main():
    intro()
    location_flat()
    location_bus_stop()
    location_codecool()
    game_finished()


main()