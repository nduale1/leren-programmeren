tafel = int(input ("Welke tafel wilt u zien?"))
print(f" Tafel van {tafel}:")
for getal in range (1,11):
    print(f"{getal} x {tafel}= {getal * tafel}")


lijst1  = [5, 12, 19, 27, 3,25]
print ("lijst: ", lijst1)
lijst1.pop(1)
print ("lijst: ", lijst1) 
lijst1.pop(0)  
print ("lijst: ", lijst1) 
lijst1.insert(0,(36))
print ("lijst: ", lijst1) 


