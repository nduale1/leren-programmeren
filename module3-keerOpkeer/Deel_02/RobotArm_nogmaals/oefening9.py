from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

robotArm.speed = 3

for stapel in range (1,5):
    for box in range (stapel):
     robotArm.grab()
     for move in range (5):
      robotArm.moveRight()
    robotArm.drop()
    for move in range ( 5 -(box ==stapel -1)):
     robotArm.moveLeft()



# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()  