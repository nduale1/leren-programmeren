#smartphone
Iphone13= int (input ('Hoeveel kost de iphone 13?'))

Samsung_s22= int (input('Hoeveel kost de Samsung Galaxy S22?'))
max = input ('Welke telefoon is duurder?')
if max == 'iphone13':
    print (f'De iphone13 is het duurst, de telefoon kost:{Iphone13}Euro')
if max == 'Samsung S22':
    print (f'De Samsung S22 is het duurst, de telefoon kost: {Samsung_s22} euro')

min = input ('Welke telefoon is goedkoper?')
if min =='iphone13':
    print (f'De iphone13 is het goedkoopst, de telefoon kost: {Iphone13} euro.')
if min == 'samsung S22': 
    print (f'De samsung S22 is het goedkoopst, de telefoon kost: {Samsung_s22} euro.')

Verschil = Iphone13 - Samsung_s22
if Verschil <=50:  
    print (f'Het advies is dus de {max} te kopen, Deze is namelijk {Verschil} euro duurder dan de {max}.') 
if Verschil >=50: 
    print (f'Het advies is dus de {min} te kopen, Deze is namelijk {Verschil} euro goedkoper dan de {max}.') 







