from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')


robotArm.speed= 2
moves = 8
for arm in range(5):
    robotArm.grab()
    for x in range (moves):
        robotArm.moveRight()
    robotArm.drop()
    moves = moves -1
    for i in range (moves):
        robotArm.moveLeft()
    
    moves = moves -1


for x in range (4):
    robotArm.moveLeft()
robotArm.grab()




# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 