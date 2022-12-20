from fruitmand import fruitmand

name= ''
color = ''
gewicht = 0
letters = 0
fruit = [i['name']for i in fruitmand if 'name' in i]

for fruit in fruitmand:
    if letters < len(fruit ['name']):
        name = fruit ['name']
        color = fruit ['color']
        gewicht = fruit ['weight']
        letters = len(fruit['name'])

print ( f" de {name} ({letters} letters) heeft een {color} kleur en een gewicht van {gewicht / 1000} kg")