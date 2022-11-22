
import time
import random
#parameters

def fprint(str, delay = 0): 
    print ("\n" + str) 
    time.sleep (delay) 



def entry():
    fprint("You're in the forest and it is dark. You can't see a lot but hear the zombies from far.",2)
    fprint ("Ahead you will see a house",2)

    return ("choosehouse")


def choosehouse():
    while house != "1" and house != "2":
        house= ("Will you enter the house? choose 1 for YES and 2 for NO ")
        return "checkhouse"

def checkhouse (choosehouse):
   
   correcthouse = random.randint(1, 2)
   
   if choosehouse == correcthouse:
        fprint ("You picked the right choice. The zombies didn't hear you and arrived at the house safely",2)
        return "room1"
   else : 
        gameover ("You go back and there was a zombie waiting for you outside, and attacks you immediatly.")
        return "Gameover"


def room1():
    fprint("You enter the house and hear people wishpering, You try to follow the voices",2)
    fprint("The corridor ends, you have to choose if you want to go right or left",2)
   
def ChooseRoom():
    while choice != "1" and choice != "2":
        choice = "Which path will you choose, right or left. Choose 1 for LEFT and 2 for RIGHT"
        return "checkroom"

def checkroom (chooseroom):
    correcthouse = random.randint(1, 2)

    if choosehouse == correcthouse:
        print
        return "rescued"
    else : 
        gameover ("""left> You go to the left. The light goes out and you can't see anything. You try to use your other insticts such as
         feeling things, But unfortunally you hand goes in the mouth of a zombie and you get infected.""")
        return "Gameover"

   
def rescued():
    fprint("You were losing the fight and almost became zombie food. But luckily someone came to help and sliced the zombie with a samurai",2)
    return"Victory"
        
def victory():
    fprint("You're grateful to have found this group.",2)
    fprint("They have saved your life on multiple occasions. With their help you finnaly reach the safe place, the place without any zombies.",2)
    print(">>YOU HAVE WON THE GAME<<")

def gameover(title):
    print(title)
    print ("GAME OVER.")


choice = entry()

while True:
        if choice == "choosehouse":
            choice = choosehouse()
        if choice == "checkhouse":
            choice = checkhouse()
        if choice == "room1":
            choice = room1()
        if choice == "checkroom":
            choice = checkroom()
        if choice == "rescued":
            choice = rescued()
        if choice == "victory":
            choice = victory()








#main - antwoord, parameters
#parameters
#functions - Vraag, antoowrd


