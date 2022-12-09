land1 = input("Land1:")
land2 = input("Land2:")
land3 = input("Land3:")

score_land1 = 0
score_land2 = 0
score_land3 = 0

voor_land1 = 0 
voor_land2 = 0
voor_land3 = 0

tegen_land1 = 0 
tegen_land2 = 0
tegen_land3 = 0

print("Wedstrijd 1")
doelpunten_land1 = int(input(f"doelpunten {land1}"))
doelpunten_land2 = int(input(f"doelpunten {land2}"))

voor_land1 += doelpunten_land1
tegen_land1 += doelpunten_land2
voor_land2 += doelpunten_land2
tegen_land2 += doelpunten_land1

if doelpunten_land1 > doelpunten_land2:
    score_land1 += 3   

else:
    score_land2 += 3


print(f"{land1} : {score_land1} +doelpunten:  {voor_land1} tegen: {tegen_land1}")
print(f"{land2} : {score_land2} +doelpunten:  {voor_land2} tegen: {tegen_land2}")
print(f"{land3} : {score_land3} +doelpunten:  {voor_land3} tegen: {tegen_land3}")

print("Wedstrijd 2")
doelpunten_land1 = int(input(f"doelpunten {land1}"))
doelpunten_land3 = int(input(f"doelpunten {land3}"))

voor_land1 += doelpunten_land1
tegen_land1 += doelpunten_land3
voor_land3 += doelpunten_land3
tegen_land3 += doelpunten_land1

if doelpunten_land1 > doelpunten_land3:
    score_land1 += 3   
else:
    score_land3 += 3


print(f"{land1} : {score_land1} +doelpunten:  {voor_land1} tegen: {tegen_land1}")
print(f"{land2} : {score_land2} +doelpunten:  {voor_land2} tegen: {tegen_land2}")
print(f"{land3} : {score_land3} +doelpunten:  {voor_land3} tegen: {tegen_land3}")


print("Wedstrijd 3")
doelpunten_land2 = int(input(f"doelpunten {land2}"))
doelpunten_land3 = int(input(f"doelpunten {land3}"))


if doelpunten_land2 > doelpunten_land3:
    score_land2 += 3   
else:
    score_land3 += 3
    

voor_land2 += doelpunten_land2
tegen_land2 += doelpunten_land3
voor_land3 += doelpunten_land3
tegen_land3 += doelpunten_land2


print(f"{land1} : {score_land1} +doelpunten:  {voor_land1} tegen: {tegen_land1}")
print(f"{land2} : {score_land2} +doelpunten:  {voor_land2} tegen: {tegen_land2}")
print(f"{land3} : {score_land3} +doelpunten:  {voor_land3} tegen: {tegen_land3}")