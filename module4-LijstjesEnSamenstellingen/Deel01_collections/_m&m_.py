import random

kleur= ("rood","blauw","geel","groen","bruin")

(rood,blauw,geel,groen,bruin) = kleur 

Aantal = int(input("Hoeveel m&m's wilt u?"))
set = (random.choices(kleur, k= Aantal))

print("Er zijn m&m's toegevoegd aan")
print (set) 

# for x in range (Aantal):
#    set.append(random.choice(kleur))