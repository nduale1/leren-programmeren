# Welke kaas ben jij?  
# 'welke kaas ben jij?' is een hele leuke spel die erg op 'Wie is het lijkt'. 
# Je kan minimaal met 2 personen spelen en maximaal met 4.

print ('Spelregels') 
Start =  input ('Wilt u gaan starten met het spel?')  

Antwoord2 = input ('Is de kaas geel?')
if Antwoord2 == 'ja':
    Antwoord6= input ('zitten er gaten in?') 
    if Antwoord6 == 'ja':
        antwoord7= input ('is de kaas belachelijk duur?') 
    if antwoord7 == 'ja':
        print ( 'Je bent de kaas emmenthaler')
        if antwoord7 == 'nee':
            print ('je bent de kaas leerdammer')
    elif  Antwoord6 == 'nee': 
        Antwoord8 = input ('is de kaas hard als steen?')
        if Antwoord8 == 'ja':
            print ( 'je bent de kaas pramigiano reggiano')
        if Antwoord8 == 'nee':
            print ('je bent de kaas Goudse kaas') 
elif   Antwoord2 == 'nee': 
        Antwoord4 = input ('Heeft de kaas blauwe schimmel?')
        if Antwoord4 == 'nee':
            Antwoord12 = input ('Heeft de kaas een korst?')
            if Antwoord12 == 'ja':
                print ('Je bent de kaas Camembert')
                if Antwoord12 == 'nee':
                    print ('je bent de kaas Mozarella' )
                    if Antwoord4 == 'ja':
                        Antwoord14 = input ('heeft de kaas een korst?')
                        if Antwoord14 == 'ja':
                            print ('Je bent de kaas Blue de Rochbaron')
                            if Antwoord14 == 'nee': 
                                print ('je bent de kaas Foumme dAmbert')

