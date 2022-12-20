from fruitmand import fruitmand

fruitmand.remove ({
    'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True

})

kleuren = [i['color']for i in fruitmand if 'color' in i]

verschillende_kleuren= [] 


for i in kleuren:
    if i in verschillende_kleuren:
        continue
    else:
        print (i)
    verschillende_kleuren.append(i)