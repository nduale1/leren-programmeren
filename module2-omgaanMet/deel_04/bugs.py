import random

name = input ('Wat is jouw naam?')
print('Hallo', name)


favoriteSeason = input ( 'Wat is jouw favorite seizoen? a) Lente, b) Zomer, c) Herfst of d) Winter')
answer = favoriteSeason.lower()

if answer == 'a': 
    print("Ik hou ook van de lente!")
elif answer == 'b':
    print("De zomer is voor mij te warm.") 
elif answer == 'c':
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == 'd':
    print("Is de winter niet erg koud?")
else:
    print("Die ken ik niet...")

favoriteColor = input('En wat is je favoriete kleur? ') 
randomcreate = random.randint(0,1)

if randomcreate == 0 :
    print('Ik vind dat ook een mooie kleur!') 
elif randomcreate == 1 : 
    print('TBH, ik hou niet zo van {}...' . format(favoriteColor)) 

 
num1 =  random.randint (1,10) 
num2 =  random.randint (5,15)
   
number =  input (f'En weet jij wat {num1} + {num2} is?')
try:
    if int (number) == num1 + num2:
        print('Dat is juist')   
    else:
        print ('Nee dat klopt niet'. format (name)) 
except:
    print ('Dat is geen nummer!')  
    