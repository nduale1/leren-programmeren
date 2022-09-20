#speelhal.py
personen = int (input('met hoeveel personen ben je?'))
ticket = 745
ticketprijs = ticket * personen
tijd = int (input('hoeveel minuten wil je de vr gebruiken?'))
vr = tijd / 5 * 0.37 * personen
totaal = int(input( ticketprijs + vr ))
print ( 'totaal', totaal 'cent')
print (f' Dit geweldige dagje-uit met {personen} in de Speelhal met {tijd} kost je maar {totaal}" ) 
