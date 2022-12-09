import random

Colors= ("rood","blauw","geel","groen","bruin")

hoeveel = int(input("Hoeveel m&m's moeten er toegevoegd worden?"))

Tas = {




}
getal = 1

for x in range (hoeveel):
    kleur = random.choice(Colors)
    if kleur not in Tas:
        Tas.update({kleur:getal})
    elif kleur in Tas:
        Tas [kleur] +=1


print(Tas)
