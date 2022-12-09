# name of student: Nedja
# number of student: 
# purpose of program: wissel geld berekenen en teruggeven
# function of program: Munten waarde geven en wisselgeld berekenen
# structure of program: functioneert door het gebruik van if's, while loops en variabelen



toPay = int(float(input('Amount to pay: '))* 100)   # Je vraagt met behulp van een int hoeveel klant moet betalen
paid = int(float(input('Paid amount: ')) * 100)     #Je vraagt met behulp van een int hoveel euro klant heeft terug gegeven
change = paid - toPay #

Vijf_Euro = 500
Drie_Euro = 300
Twee_Euro = 200
Vijftig_Cent = 50
Twintig_Cent = 20
Tien_Cent = 10
Vijf_Cent = 5
Twee_cent= 2
Een_Cent = 1

if change > 0: #  Als de wisselgeld boven de 0 is print hij :
  coinValue = 500 # Dan is de Value 50
  
  while change > 0 and coinValue > 0: #  hier s,tart de while loop
    nrCoins = change // coinValue #   berekening om nrcoins te krijgen

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Hoeveel munten van coinvalue kan geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Hier wilt hij weten hoeveel coins je wilt
      change -= nrCoinsReturned * coinValue #Aantal ingevoerde coins x de coinvalue = de change

# comment on code below: 
    if coinValue == Vijf_Euro:
      brood = nrCoinsReturned
      coinValue = Drie_Euro
    elif coinValue == Drie_Euro: 
      brood_lang = nrCoinsReturned
      coinValue = Twee_Euro
    elif coinValue == Twee_Euro: 
      brood_breed = nrCoinsReturned
      coinValue = Vijftig_Cent
    elif coinValue == Vijftig_Cent: 
      brood_klein =  nrCoinsReturned
      coinValue = Twintig_Cent
    elif coinValue == Twintig_Cent:  
      brood_volkoren = nrCoinsReturned
      coinValue = Tien_Cent
    elif coinValue == Tien_Cent:
      brood_wit = nrCoinsReturned
      coinValue = Vijf_Cent
    elif coinValue == Vijf_Cent:
      brood_bruin = nrCoinsReturned
      coinValue = Twee_cent
    elif coinValue == Twee_cent:
      brood_tijger = nrCoinsReturned
      coinValue = Een_Cent
    else:
      coinValue = 0
     
try:

 if change > 0: # Als de wisselgeld boven de 0 is print hij :
  print('Change not returned: ', str(change) + ' cents')
 else:
  print(f"{Vijf_Euro} : {brood}") 
  print(f"{Drie_Euro} : {brood_lang}") 
  print(f"{Twee_Euro} : {brood_breed}") 
  print(f"{Vijftig_Cent} : {brood_klein}") 
  print(f"{Twintig_Cent} : {brood_volkoren}") 
  print(f"{Tien_Cent} : {brood_wit}") 
  print(f"{Vijf_Cent} : {brood_bruin}") 
  print(f"{Twee_cent} : {brood_tijger}") 
except NameError:
  exit()