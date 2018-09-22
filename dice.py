#                                           --- Dice simulator 2018 by Ducc ---
import random
import operator

#Variables
d_number = 0
dm_number = 0
d_numberslot1 = "N/A"
d_numberslot2 = "N/A"
d_numberslot3 = "N/A"
d_numberslot4 = "N/A"
d_numberslot5 = "N/A"
user = "" #(User input)
helplist = """--- Commands ---
\u2023 !help
\u2023 !roll
\u2023 !rollmultiple
\u2023 !history
\u2023 !about\n"""
running = True
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
#nma = 0 #number most appeared [OBSOLETE]

#Functions
def roll():
    global d_number
    global d_numberslot1
    global d_numberslot2
    global d_numberslot3
    global d_numberslot4
    global d_numberslot5

    print("Rolling the dice...")
    d_number = random.randint(1,6)
    d_numberslot5 = str(d_numberslot4)
    d_numberslot4 = str(d_numberslot3)
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
        print("[ATTENTION: only shows stats for single roll, not multiple roll]")
        print("Last 5 numbers: {} , {} , {} , {} , {}".format(d_numberslot1,d_numberslot2,d_numberslot3,d_numberslot4,d_numberslot5))
        menu_r()
        
    elif user == "!about":
        print("\n\u2043 Made by Pedro Henrique Rincon Santos (Ducc) \u2043\n")
        menu_r()
        
    elif user == "!rollmultiple":
        m_roll()
        
    else:
        print("Unknown command")
        menu_r()

def m_roll():
    global dm_number
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    n1,n2,n3,n4,n5,n6 = 0,0,0,0,0,0
    dicenumber = 1
    dm_number = 0
    user2 = input("How many dices would you like to roll?\n> ")
    user2 = int(user2) + 1        
    for number in range(1,user2):
        dm_number = random.randint(1,6)
        print("Dice {0} = {1}".format(dicenumber,dm_number))
        dicenumber += 1
        n_counter()
    print("\n---- Stats: ----\nTimes number one appeared: {}\nTimes number two appeared: {}\nTimes number three appeared: {}\nTimes number four appeared: {}\nTimes number five appeared: {}\nTimes number six appeared: {}".format(n1,n2,n3,n4,n5,n6))
    menu_r()
                   
def menu_r():
    if running == True:
        menu()

def n_counter():
    global dm_number
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    dm_number -= 1
    if dm_number == 1:
        n1 += 1
    elif dm_number == 2:
        n2 += 1
    elif dm_number == 3:
        n3 += 1
    elif dm_number == 4:
        n4 += 1
    elif dm_number == 5:
        n5 += 1
    elif dm_number == 6:
        n6 += 1
    else:
        print("COUNTER ERROR, report this bug to https://github.com/BlackmanWhite/DiceSimulator2018/issues")
        print("dm_number = {}".format(dm_number))
        return None

#Main
print("\u25ba ---------- Dice Simulator 2018\u2122 ---------- \u25c4")
print("Welcome user! type !help to see more commands\nTip: Type !roll to roll the dice")
menu()
