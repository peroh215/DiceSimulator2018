#                                              --- Dice simulator 2018 by Ducc ---
import random

#Variables
d_number = 0
d_numberslot1 = "N/A"
d_numberslot2 = "N/A"
d_numberslot3 = "N/A"
user = "" #(User input)
helplist = """--- Commands ---
\u2023 !help
\u2023 !roll
\u2023 !rollmultiple
\u2023 !history
\u2023 !about\n"""
running = True

#Functions
def roll():
    global d_number
    global d_numberslot1
    global d_numberslot2
    global d_numberslot3

    print("Rolling the dice...")
    d_number = random.randint(1,6)
    d_numberslot3 = str(d_numberslot2)
    d_numberslot2 = str(d_numberslot1)
    d_numberslot1 = str(d_number)
    print("You rolled {}!".format(d_number))

def menu():
    user = input("> ")

    if user == "!roll":
        roll()
        menu_r()
        
    elif user == "!help":
        print(helplist)
        menu_r()
        
    elif user == "!history":
        print("Previous number: {}\nPenultimate number: {}\nAntepenult number: {}".format(d_numberslot1,d_numberslot2,d_numberslot3))
        menu_r()
        
    elif user == "!about":
        print("\n\u2043 Made by Pedro Henrique Rincon Santos (Ducc) \u2043\n")
        menu_r()
        
    elif user == "!rollmultiple":
        dicenumber = 1
        d_number = 0
        user2 = input("How many dices would you like to roll?\n> ")
        user2 = int(user2) + 1
        for number in range(1,user2):
            d_number = random.randint(1,6)
            print("Dice {0} = {1}".format(dicenumber,d_number))
            dicenumber += 1             
        menu_r()
    else:
        print("Unknown command")
        menu_r()
                   
def menu_r():
    if running == True:
        menu()

#Main
print("\u25ba ---------- Dice Simulator 2018\u2122 ---------- \u25c4")
print("Welcome user! type !help to see more commands\nTip: Type !roll to roll the dice")
menu()
