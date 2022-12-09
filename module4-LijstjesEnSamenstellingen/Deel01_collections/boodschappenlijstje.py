tas = {}

while True:
    toevoegen= input("Wilt u een item toevoegen?")
    if toevoegen == 'nee':
        break 


    product = input ("Welke producten wilt u toevoegen?")
    Aantal = int(input (f"Hoeveel {product} wilt u?"))

    if product not in tas:
        tas.update({product : Aantal})

print ("---[boodschappenlijst]---")
for keys, value in tas.items():
    print(f"{value} x {keys}")
print("--------------------------")