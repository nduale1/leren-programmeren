from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1

for x in range (0,7):
    robotArm.moveRight()
    robotArm.grab()
    for x in range(0,8):
        robotArm.moveRight()
    robotArm.drop()
    for x in range (0,9):
        robotArm.moveLeft()

# x = 0 
# while True:
#     x +1
#      robotArm.grab() 
#      robotArm.moveRight()
#      robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 