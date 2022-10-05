# Welke kaas ben jij?  
# 'welke kaas ben jij?' is een hele leuke spel die erg op 'Wie is het lijkt'. 
# Je kan minimaal met 2 personen spelen en maximaal met 4.

print ('Spelregels') 
Start =  input ('Wilt u gaan starten met het spel?')  

Geel = input ('Is de kaas geel?')
if Geel == 'ja':
    Gaten= input ('zitten er gaten in?') 
    if Gaten == 'ja':
        Duur= input ('is de kaas belachelijk duur?') 
        if Duur == 'ja':
             print ( 'Je bent de kaas emmenthaler')
        elif Duur == 'nee':  #Elif in plaats van if. Hoort bij elkaar 
            print ('je bent de kaas leerdammer')
    elif  Gaten == 'nee': 
        Hard = input ('is de kaas hard als steen?')
        if Hard == 'ja':
            print ( 'je bent de kaas pramigiano reggiano')
        elif Hard == 'nee':
            print ('je bent de kaas Goudse kaas') 
elif   Geel == 'nee': 
        Antwoord4 = input ('Heeft de kaas blauwe schimmel?') # Betere namen voor betekenis 
        if Antwoord4 == 'nee':
            Antwoord12 = input ('Heeft de kaas een korst?')
            if Antwoord12 == 'ja':
                Geur = input ('Stinkt de kaas?')
                if Geur == 'ja':
                    print ('Je bent de kaas Camembert')
                elif Geur == 'nee':
                    print ('Je hebt de kaas Brie')
             
            if Antwoord12 == 'nee':
                    print ('je bent de kaas Mozarella' )
                    if Antwoord4 == 'ja':
                        Antwoord14 = input ('heeft de kaas een korst?')
                        if Antwoord14 == 'ja':
                            print ('Je bent de kaas Blue de Rochbaron')
                            if Antwoord14 == 'nee': 
                                print ('je bent de kaas Foumme dAmbert')


