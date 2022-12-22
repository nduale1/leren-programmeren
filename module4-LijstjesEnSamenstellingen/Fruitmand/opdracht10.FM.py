from fruitmand import fruitmand
naamNgewicht= {}

for fruit in fruitmand:
    naamNgewicht[fruit['name']] = fruit ['weight']
    print(naamNgewicht) 
    