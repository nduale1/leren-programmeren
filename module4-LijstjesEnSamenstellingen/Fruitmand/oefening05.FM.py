from fruitmand import fruitmand
import random 

fruit = [i['name']for i in fruitmand if 'name' in i]

for x in fruit[8::-1]:
    print(x)
