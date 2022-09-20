#speelhal.py
personen = int (input('met hoeveel personen ben je?'))
ticket = 7,45
ticketprijs = personen * ticket

tijd = int (input('hoeveel minuten wil je de vr gebruiken?'))
vr = tijd / 5 * personen

totaal = int (input(ticketprijs + vr))
print ('Totaal', totaal ,'euro') 