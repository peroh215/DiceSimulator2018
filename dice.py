import sys
import random

#Variables
d_number = 0
d_numberslot1 = "N/A"
d_numberslot2 = "N/A"
d_numberslot3 = "N/A"
user = "" #(User input)
aboutmsg = "\n\u2043 Made by Pedro Henrique Rincon Santos (Ducc) \u2043\n"
running = True

#Functions
def roll():
    global d_number
    global d_numberslot1
    global d_numberslot2
    global d_numberslot3

    print("Rolling the dice...")
    d_number = random.randint(1,6)
    d_numberslot3 = d_numberslot2
    d_numberslot2 = d_numberslot1
    d_numberslot1 = d_number
    print("You rolled {}!".format(d_number))

def menu():
    user = input("> ")

    if user == "!roll":
        roll()
        menu_r()        
    elif user == "!help":
        print("""--- Commands ---
\u2023 !help
\u2023 !roll
\u2023 !history
\u2023 !about\n""")
        menu_r()        
    elif user == "!status":
        print("Running = ",running,"\n")
        menu_r()
    elif user == "!history":
        print("Previous number: {}\nPenultimate number: {}\nAntepenult number: {}".format(d_numberslot1,d_numberslot2,d_numberslot3))
        menu_r()
    elif user == "!about":
        print(aboutmsg)
        menu_r()
        

def menu_r():
    if running == True:
        menu()

print("\u25ba ---------- Dice Simulator 2018\u2122 ---------- \u25c4")
print("Welcome user! type !help to see more commands")
print("Tip: Type !roll to roll the dice")
menu()


    
    
