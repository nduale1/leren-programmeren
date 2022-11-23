
import time
import random
#parameters

def fprint(str, delay = 0): 
    print ("\n" + str) 
    time.sleep (delay) 



def displayintro():
    fprint("It has been a year since the zombie apocalypse started",2)
    fprint ("You have been through a lot",2) 
    fprint ("You ended up alone in a forest and you have to find a way to survive.",2)
    fprint("After walking for a day you finally see a house.",2)


def choosehouse():
    house = "0"
    while house != "1" and house != "2":
        house= input ("Will you enter the house? choose 1 for YES and 2 for NO ")
    return house
  

def checkhouse (choosehouse):
   
   if choosehouse == "1":
     return True
   else:
     return False 
       

def room1():
    fprint("You enter the house and hear people wishpering, You try to follow the voices",2)
    fprint("The corridor ends, you have to choose if you want to go right or left",2)

   
def ChooseRoom():
    direction = "0"
    while direction != "1" and direction != "2":
        direction = input("Which path will you choose, right or left. Choose 1 for LEFT(1) or 2 for RIGHT(2) ")
    return direction

def checkroom (chooseroom):
    
    correctroom = random.randint(1, 2)

    if chooseroom == correctroom:
     return True
    else:
     return False 
  

   
def rescued():
    fprint("You were losing the fight and almost became zombie food. But luckily someone came to help and sliced the zombie with a samurai",2)

        
def victory():
    fprint("You're grateful to have found this group.",2)
    fprint("They have saved your life on multiple occasions. With their help you finnaly reach the safe place, the place without any zombies.",2)
    print(">>YOU HAVE WON THE GAME<<")


def gameover(title):
    print(title)
    print ("GAME OVER.")


displayintro()

house = choosehouse()
correcthouse = checkhouse(house)
while correcthouse == True:
    fprint ("You picked the right choice. The zombies didn't hear you and you arrived at the house safely",2)
    room1()
    direction = ChooseRoom()
    correctroom = checkroom(direction)
    if ChooseRoom == True:
     fprint("""The floor creeks and emmediatly you hear foot staps running towards you.
        You look behind and see the zombie is about to jump on you.
        You have to be fast and try to fight the zombie off of you.""")
     rescued()          
    else:
        gameover ("""You go to the left. The light goes out and you can't see anything. 
        You try to use your other insticts such as feeling things, But unfortunally you hand goes in the mouth of 
        a zombie and you get infected.""")   
        PlayAgain = input( "do you want to play again?")
        if PlayAgain == "yes" or "y":
         displayintro()
         choice = choosehouse()
    checkhouse(choice)      
else:
    gameover("You go back and there was a zombie waiting for you outside, and attacks you immediatly.")
    PlayAgain = input( "do you want to play again?")
    if PlayAgain == "yes" or "y":
     displayintro()
     choice = choosehouse()
    checkhouse(choice) 



rescued()
victory()



PlayAgain = input( "do you want to play again?")
while PlayAgain == "yes" or "y":
    displayintro()
    choice = choosehouse()
    checkhouse(choice) 
#while 


    












#main - antwoord, parameters
#parameters
#functions - Vraag, antoowrd
