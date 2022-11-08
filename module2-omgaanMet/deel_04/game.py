Startspel = input ('Wil je beginnen met spelen?(ja/nee)')
if Startspel.lower().strip() == "ja":
    print ("This year ")

    kruispunt = input ('Je bent aangekomen bij een kruispunt. Ga je naar link of rechts?').lower().strip() 
    if kruispunt== "links":
        monster = input ("je komt een monster tegen. kies je voor rennen of aanvallen?").lower().strip() 
        if monster == "aanvallen":
            print("Dat had je toch niet moeten doen, je hebt verloren!")
    
        else:
            print ("goede keuze, je bent nu veilig.")
    elif kruispunt == "rechts":
        print("je hebt helaas verloren, om dat het te donker was ben je tegen een boom aangekomen.")
    
    else:
        print ("niet juist, je hebt verloren!")

else:
    print ('Dat is jammer :(')
