#!/usr/bin/env python
## -*- coding: utf-8 -*-

'''
File name: dice_simulator_18
Version: 1.3.2.1
Author: Blackman White                    
Date created: 9/20/2018              
Date last modified: 10/11/2018        
Python Version: 3.7
'''

# Imports
import random
import sys

# Variables
d_number = 0
dm_number = 0
d_numberslot1 = "N/A"
d_numberslot2 = "N/A"
d_numberslot3 = "N/A"
d_numberslot4 = "N/A"
d_numberslot5 = "N/A"
user = "" # User input
helplist = """--- Commands ---
\u2023 !help
\u2023 !roll
\u2023 !rollmultiple
\u2023 !logs
\u2023 !about
\u2023 !exit\n"""
running = True
version = ("v1.3.2.1")
n1=n2=n3=n4=n5=n6=0 #Sets multiple variables to 0 in one line

# Functions
def roll():
    global d_number
    global d_numberslot1
    global d_numberslot2
    global d_numberslot3
    global d_numberslot4
    global d_numberslot5
    global d_numberslot6

    print("Rolling the dice...")
    d_number = random.randint(1,6)
    d_numberslot6 = str(d_numberslot5)
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
        return menu_r()
        
    elif user == "!help":
        print(helplist)
        return menu_r()
        
    elif user == "!logs":
        print("[ATTENTION: Only shows stats for single roll]")
        print("Last 5 numbers: {} , {} , {} , {} , {} , {}".format(d_numberslot1,d_numberslot2,d_numberslot3,d_numberslot4,d_numberslot5,d_numberslot6))
        return menu_r()
        
    elif user == "!about":
        print("\n\u2043You are running Dice Simulator 2018 {}\u2023".format(version))
        print("License: GNU GENERAL PUBLIC LICENSE Version 3 (29 June 2007)")
        print("\u2043 Made by Pedro Henrique Rincon Santos (Ducc / Blackman White) \u2043\n")
        return menu_r()
        
    elif user == "!rollmultiple":
        return m_roll()
        
    elif user == "!exit":
        return sys.exit(0)
        
    else:
        print("Unknown command")
        return menu_r()

def m_roll():
    global dm_number
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    n1=n2=n3=n4=n5=n6=0
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
    return menu_r()
                   
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

# Main
print("\u25ba ---------- Dice Simulator 2018\u2122 ---------- \u25c4")
print("Welcome user! type !help to see more commands\nTip: Type !roll to roll the dice")
menu()
