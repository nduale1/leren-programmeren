""
# The Zombie Apocalypse!

print ('''Zombies are evreywhere!!
They are trying to invade your house.
And you are alone''')

# To start the game you need to creat your character first.


name= input ('What'')

print ('''
What are you going to do?
1. Fight the zombies with a baseball bat.
2. Play dead
3. Run to the nearest hiding place
4. Call 112
''')

Choice = input ("You choose:")

if Choice.strip ()[0] == "1":
    print ('''You fight vigrously. You manage to knock down 3 zombies, 
    but then another zombie came from behind ... and you are dead.''')
elif Choice.strip()[0] == "2":
    print ('''Ýou play dead. The zombies do not notice you at all. 
    but then, you have a strong urge to sneeze, and as soon as you sneeze... you are dead.''')
elif Choice.strip()[0] == "3":
    print (''''You run to the treehouse. There you find your friends hiding as well. You are safe.
    But then... there is no water or food in the treehouse, so you starve to death.''')
elif Choice.strip()[0] == "4":
    print ('''You call 112. The operator answer, but the operator is only screaming. He is dead. You are also dead.''')
else: 
    print ('please choose 1, 2, 3 or 4')

>help

