from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

teller = 9
for x in range (0,9):
    robotArm.grab()
    color= robotArm.scan()
    if color == "red":
        for x in range (teller):
            robotArm.moveRight()
        robotArm.drop()
        for x in range (teller -1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    teller -=1







# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()     