from fruitmand import fruitmand
rond= 0
nietrond=0

x= False
while x == False:
    kleur = input ("kies een kleur")
    for fruit in fruitmand:
        if fruit ['color'] == kleur:
            x = True 

        if fruit ['round'] == True:
            rond +=1 

        else:
            nietrond +=1
        if rond > nietrond:
            print(f"Er zijn {rond - nietrond} meer ronde vruchten dan niet ronde vruchten in kleur {kleur}")
        elif rond < nietrond:
            print(f"Er zijn {nietrond - rond} minder ronde vruchten dan niet ronde vruchten in kleur {kleur}")
        elif rond == nietrond:
             print(f"Er zijn {rond} ronde vruchten en {nietrond} niet ronde vruchten in kleur {kleur}")
        exit()

    else:
        print(f"{kleur} zit er niet in")
