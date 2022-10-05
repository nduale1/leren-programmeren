

#Nedja Duale opdracht: pizzaCalculator 

try :
    pizzasmall= int (input ('hoeveel pizzasmall wilt u?'))
except ValueError: 
    print ('Er ging iets fout, probeer het nog eens. Voer volgende keer een cijfer i.p.v letters')

try :
    pizzamedium= int (input ('hoeveel pizzamedium wilt u?'))
except ValueError: 
    print ('Er ging iets fout, probeer het nog eens. Voer volgende keer een cijfer i.p.v letters')

try :
    pizzalarge= int (input ('hoeveel pizzalarge wilt u?')) 
except ValueError: 
    print ('Er ging iets fout, probeer het nog eens. Voer volgende keer een cijfer i.p.v letters') 


#whileTrue , #break 
#while (True):  
    #pizzasmall= int (input ('hoeveel pizzasmall wilt u?'))
    #except ValueError: 
    #print ('Er ging iets fout, probeer het nog eens. Voer volgende keer een cijfer i.p.v letters')

prijssmall= pizzasmall * 4.99
prijsmedium= pizzamedium * 6.99
prijslarge= pizzalarge * 11.99

totaal = prijssmall + prijsmedium + prijslarge 
print('')
print('Totale prijs:' )

print (' --------------------' )
print ( f'| {prijssmall}')           
print ( f'| {prijsmedium}') 
print ( f'| {prijslarge}')
print ( f'  -------------- =')
print ( f'  {totaal} euro ')
