Days= ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"] 

print ("Alle dagen van de week zijn:")
for x in Days:
    print(x)

print()

print("Alle werkdagen van de week zijn:")
for x in Days[0:5]:
    print (x)

print()

print("De weekend dagen zijn:")
for x in Days[5:7]:
    print(x)

print()

print ("Alle dagen van de week in omgekeerd volgorde:")
for x in reversed (Days):
    print(x)

print()

print("Werkdagen in omgekeerde volgorde: ")
for x in reversed(Days[0:5]):
    print(x)

print()

print("Weekend dagen in omgekeerde volgorde: ")
for x in reversed(Days[5:7]):
    print(x)