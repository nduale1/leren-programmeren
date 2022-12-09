import random

Aantal_rondes=20
Aantal_pogingen = 10
poging = 0
ronde = 0
punten = 0


while ronde < Aantal_rondes:
    raden = input("wil je starten met raden?")

    if raden == "nee":
        print("Nou, je bent in ieder geval wel eerlijk :)")
        print (f"Jou aantal punten zijn {punten} van de {Aantal_rondes}")
        exit()
    
    num = random.randint(1, 1000)
    while poging < Aantal_pogingen:
        while True:
            try:
                answer = int (input("Raad het getal > "))
                break
            except ValueError:
                print("ERROR, Vul alleen cijfers in!!!")

        if answer == num:
            print("Dat is knap! je hebt het helemaal goed :0")
            if Aantal_rondes == 20:
                print("Jammer :( je was zo dichtbij!")
            punten += 1
            break
        else:
            verschil = abs (answer - num)
            if verschil <= 20:
                print ("HEET HEET! Je bent heel erg warm")
            elif verschil <= 50 and verschil >= 20:
                print("je bent warm..!")
        poging +=1

    print (f" je hebt een {punten} gescoord")
    ronde +=1
    poging = 0
        
