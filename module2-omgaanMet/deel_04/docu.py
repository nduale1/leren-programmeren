Naam = input ('Wat is uw volledige naam?')
if Naam == 'jan pieter':
    raise NameError ('Helaas jan pieter, op basis van jouw naam weten wij al genoeg. Gelieve ergens anders te soliciteren.')


Aantal_jaar_ervaring = False
De_Perfecte_Gewicht = False
De_perfecte_lengte= False


Ervaring= input ('Waar heeft u ervaring in: dieren-dressuur, jongleren of Acrobatiek?')
if Ervaring == ('dieren_dressuur'):
    Praktijkervaring1 = int (input ('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?') ) 
    if Praktijkervaring1 >= 4: 
        Aantal_jaar_ervaring = True     

if Ervaring == ('jongleren'):
    praktijkervaring2 = int (input ('Hoeveel jaar praktijkervaring heeft u met jongleren?'))
    if praktijkervaring2 >= 3: 
        Aantal_jaar_ervaring = True

if Ervaring == ('acrobatiek'):
    praktijkervaring3= int (input ('Hoeveel jaar praktijkervaring heeft u met acrobatiek'))     
    if praktijkervaring3 >= 5: 
        Aantal_jaar_ervaring = True

Diploma= input ('Bent u in bezit van diploma mbo4 ondernemen?')
if Diploma == 'nee':
   raise ValueError ('Sorry hoor, maar wat had je verwacht. Bij ons bedrijf gelt het volgende: geen diploma, geen baan')

rijbewijs= input ('Bent u in bezit van een geldige vrachtwagen rijbewijs?')

certificaat= input ('Heeft u een certificaat voor werken met gevaarlijke personeel?')
if certificaat == 'nee':
    raise ValueError ('Helaas dat gaat voor ons niet werken.')
    
Hoge_hoed= input ('Bent u in het bezit van een hoge hoed?')

Gewicht = int (input ('Wat is uw gewicht?'))
if Gewicht >= 90 and Gewicht <= 120: 
    De_Perfecte_Gewicht= True


Lengte = int (input ('Hoe lang bent u?'))  
if Lengte >= 150 and Lengte <= 220 : # de 'And' kan je toevoegen 
    De_perfecte_lengte = True


Heeft_goede_snor = False
Heeft_goed_haar = False 

Geslacht= input ('Wat is uw geslacht?')

if Geslacht == 'man': 
    snor = input ('heeft u een snor?')
    if snor == 'ja':
        snorbreedte= int (input ('hoe breed is uw snor?'))
        if snorbreedte >= 10: 
            Heeft_goede_snor = True

else: 
    if Geslacht == 'vrouw':
        Haar= input ('Heeft u rood haar?')
        if Haar == 'ja': 
             Haar_type= ('Wat voor type haar heeft u? ')
             if Haar_type == 'krullen': 
                Haar_kleur= input ('Wat is uw haarkleur?')
                if Haar_kleur == 'rood':
                    Haar_lengte= int (input ('Wat is uw haar lengte?'))
                    if Haar_lengte >= 10:
                        Heeft_goed_haar = True 

if (Heeft_goede_snor or Heeft_goed_haar) and Aantal_jaar_ervaring and De_Perfecte_Gewicht and De_perfecte_lengte : 
    print ('U bent aangenomen!')
else:
    print ('Helaas bent u niet aangenomen :(')  
    