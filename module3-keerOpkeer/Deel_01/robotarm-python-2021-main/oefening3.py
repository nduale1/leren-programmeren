from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:

robotArm.grab()

for x in range (0,3):
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.grab() 
   
robotArm.moveRight()
robotArm.drop()




    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
