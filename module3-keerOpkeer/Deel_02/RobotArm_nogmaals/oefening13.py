from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

robotArm.speed= 2

place = 9
move = True
while move:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        print("niks om te grijpen")
        move = False
    else: 
        for arm in range (place):
            robotArm.moveRight()
        robotArm.drop()
        for Arm in range (place):
            robotArm.moveLeft()
        place -=1
# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()