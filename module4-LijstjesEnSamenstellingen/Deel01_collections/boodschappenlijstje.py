boodschappentas = {}

while True:
    toevoegen= input("Wilt u een item toevoegen aan uw booschappentas?")
    if toevoegen == 'nee':
        break 


    product = input ("Welke product wilt u toevoegen?")
    Aantal = int(input (f"Hoeveel {product} wilt u?"))

    if product not in boodschappentas:
        boodschappentas.update({product : Aantal})

print ("---[boodschappenlijst]---")
for keys, value in boodschappentas.items():
    print(f"{value} x {keys}")
print("--------------------------") 
