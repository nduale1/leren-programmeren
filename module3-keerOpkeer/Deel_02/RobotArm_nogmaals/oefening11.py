from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

for x in range (8):
    robotArm.moveRight()

for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        if x < 8 :
            robotArm.moveLeft()
            robotArm.moveLeft()
    else:
        robotArm.drop()
        if x < 8 :
            robotArm.moveLeft()










# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()