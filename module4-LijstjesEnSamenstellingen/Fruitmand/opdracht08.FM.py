from fruitmand import fruitmand

fruitmand.append ({
    'name' : 'Watermeloen',
    'weight' : 2435,
    'color' : 'green',
    'round' : True

})

gewicht = [i['weight']for i in fruitmand if 'weight' in i]
Totaal = sum(gewicht)

print (Totaal)