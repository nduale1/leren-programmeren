from fruitmand import fruitmand 
# for i in fruitmand:
#     if 'name' in i:
#         print (i)

fruit = [i['name']for i in fruitmand if 'name' in i] 
for i in fruit:
    print (i)
