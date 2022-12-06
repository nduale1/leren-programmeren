from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 3


for x in range (3):

    for x in range(0,6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for x in range (0,2):
        robotArm.moveRight()
    for x in range(0,6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for x in range (0,2):
        robotArm.moveRight()





    

    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

# i = 1
# while <10:
#     print()