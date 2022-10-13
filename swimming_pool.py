#sstap1 
lengte = int (input("voer hier de lengte"))
breedte = int (input("voer hier de breedte"))
diepte = float (input("voer hier de diepte"))

inhoud = lengte * breedte * diepte 

print ("stap1")
print (f"{inhoud}")
print ()
print ("stap2")
#36m3

kostenuitgraven = 25
kostenafvoergrond = 32.50
uitgraven = inhoud * kostenuitgraven
afvoergrond = inhoud * kostenafvoergrond
totaal = uitgraven + afvoergrond
print (f"uitgraven:   {uitgraven} euro")
print (f"afvoeren grond:  {afvoergrond} euro")
print (f"totaal: {totaal} euro")
print ()

print ("stap3")
kostenperkilometer= 2.05
afstandzwembad = 60
voorrijkosten = afstandzwembad * kostenafvoergrond
totaal2 = uitgraven + afvoergrond + voorrijkosten
print (f"uitgraven:   {uitgraven} euro")
print (f"afvoeren grond:  {afvoergrond} euro")
print (f"voorrijkosten : {voorrijkosten} euro")
print (f"totaal: {totaal2} euro")
print ()

print ("stap4")#gedaan
print ()
print ("stap 5a")
#24m2
vierkantekm= lengte * breedte
print (f'{vierkantekm}')
print ()

print ("stap 5b")
prijsperm2= 200
prijsrood= 20
prijskeuzekleur= 125
kosten_per_m2 = vierkantekm * prijsperm2
kosten_kleur_rood= vierkantekm * prijsrood
kosten_gekozen_kleur= vierkantekm* prijskeuzekleur
beton_tegel= kosten_per_m2 + kosten_kleur_rood +kosten_gekozen_kleur
totaal3 = uitgraven + afvoergrond + voorrijkosten + beton_tegel
print (f"uitgraven:   {uitgraven} euro")
print (f"afvoeren grond:  {afvoergrond} euro")
print (f"voorrijkosten : {voorrijkosten} euro")
print (f"beton + tegel :  {beton_tegel} euro")
print (f"totaal: {totaal3} euro")
print ()





