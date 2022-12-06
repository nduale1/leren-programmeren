# name of student: N. Duale
# number of student: 
# purpose of program: 
# function of program: 
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100)   # Je vraagt met behulp van een int hoeveel klant moet betalen
paid = int(float(input('Paid amount: ')) * 100)     #Je vraagt met behulp van een int hoveel euro klant heeft terug gegeven
change = paid - toPay #

if change > 0: #  Als de wisselgeld boven de 0 is print hij :
  coinValue = 50 # Dan is de Value 50
  
  while change > 0 and coinValue > 0: #  
    nrCoins = change // coinValue #   

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20: 
      coinValue = 10
    elif coinValue == 10: 
      coinValue = 5
    elif coinValue == 5:  
      coinValue = 2
    elif coinValue == 2:  
      coinValue = 1
    else:
      coinValue = 0
     
      
if change > 0: # Als de wisselgeld boven de 0 is print hij :
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done') 