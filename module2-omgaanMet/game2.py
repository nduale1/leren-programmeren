
import time
#parameters

def fprint(str, delay = 0):
    print ("\n" + str)
    time.sleep (delay)


def entry():
    print("You're in the forest and it is dark. You can't see a lot but hear the zombies from far.",2)
    print ("Ahead you will see a house. will you continue?")
    while True:
        action= input ("\n>")
        if action == "yes":
            return "House"
        elif action == "no":
            gameover("A bat flies over your head and you hear screetches in the distance.")
            return "Gameover"
                
def House():
    
    fprint("You enter the house. It's pitch black you can't see anything. But you hear voices from the distance",2)
    print ("Will you continue or go back?")
    while True:
        action= input ("\n>")
        if action == "continue":
             return "room1"
        elif action == "go back":
            gameover("You go back and there was a zombie waiting for you outside, and attacks you immediatly.")
            return "Gameover"
        
def room1():
    fprint("The floor breaks and you fall head first into the basement.",2)
    print ("Luckily, you only landed on your back.",2)
    print("You can try to climb out. Will you try?")
    while True:
        action= input ("\n>")
        if action == "yes":
             return "attack"
        elif action == "no":
            gameover("You sit in utter darkness.")
            return("Gameover")
def attack():
        fprint("A zombie who was nearby heard the loud noise of you falling. He runs to your directions. What will you do?",2)
        print ("Are you going to attack or play dead?")
        while True:
            action= input ("\n>")
            if action == "attack":
                 return "fightback"
            elif action == "play dead":
                gameover("You play dead but the zombie already know what you smell like and attacks you.")
                return("Gameover")

def fightback():
    fprint("On the floor you will see 3 objects you can attack with, Which one will you choose?",2)
    print ("cable, pineapple, teddybear ")
    while True:
        action= input ("\n>")
        if action == "cable":
             return "rescued"
        elif action == "pineapple":
            fprint("You play dead but the zombie already knows what you smell like and attacks you.")
            print("GAME OVER.")
        elif action == "teddybear":
            gameover("The teddybear did not do much damage. The zombie is stronger and you can't fight back.")
            return("Gameover")

def rescued():
    fprint("You were losing the fight and almost became zombie food. But luckily someone came to help and sliced the zombie with a samurai",2)
    print ("The stranger asks you if you want to join his group")
    print("What will you answer him. yes or no?")
    while True:
        action= input ("\n>")
        if action == "yes":
             return "victory"
        elif action == "no":
            gameover("You don't get far and get into another fight with a zombie. But this time no one came to save you.")
        
def victory():
    print("You're grateful to have found this group.",2)
    print("They have saved your life on multiple occasions. With their help you finnaly reach the safe place, the place without any zombies.",2)
    print("YOU HAVE WON THE GAME")

def gameover(title):
    print(title)
    print ("GAME OVER.")


#main - antwoord, parameters
#parameters
#functions - Vraag, antwoord


choice = entry()

if choice == 'House':
    choice = House()
    while True:
        if choice == "room1":
            choice = room1()
        if choice == "attack":
            choice = attack()
        if choice == "fightback":
            choice = fightback()
        if choice == "rescued":
            choice = rescued()
        if choice == "victory":
            choice = victory()







