from fruitmand import fruitmand
import random

aantal= int(input("Hoeveel fruit wilt u in uw mandje?"))
fruit = [i['name']for i in fruitmand if 'name' in i]

set = (random.choices(fruit, k= aantal))


print (set) 