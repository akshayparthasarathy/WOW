"""
Take a picture, run detection, move to location. Move down 5 cm
Take another picture, run detection. 
Check if current (x,y) is close to actual (x, y). else redo line 1 onwards (max 3 times)
Move down and grab
Move to bin
"""
import wowclasses
"""
rob = urx.Robot("192.168.1.5", True)
robotiqgrip = Robotiq_Two_Finger_Gripper(rob)
"""
g = wowclasses.groceries()
height = 480
width = 640

home = [0, -1.57, -1.57, -1.57, 1.57, 0]

bin1 = [-0.20, 0.1, 0.40]
bin2 = [-0.20, -0.1, 0.40]
bin3 = [0.20, 0, 0.40]

apple = False
carrot = False
bottle = True
n=0

while apple:
    #rob.movej(home, 0.2, 0.2)
    g.capture(2)
    print("Captured picture "+str(n+1))
    location = g.detect()
    print("Detection on picture "+str(n+1)+" Complete")
    if "apple" in location and n < 2:        
        loc = location["apple"]
        x = (0.5-loc[0])*(0.64*((0.46 - 0.1*n)/0.46))
        y = (0.5-loc[1])*0.48*((0.46 - 0.1*n)/0.46)+.06
        g.move([-x, -y])
        print("moved to "+str([-x, -y]))
        n+=1
    if n == 2 and ("apple" in location):
        g.capture(2)
        print("Captured picture "+str(n+1))
        location = g.detect()
        print("Detection on picture "+str(n+1)+" Complete")

        x = (0.5-loc[0])*(0.64*((0.46 - 0.1*n)/0.46))+.03
        y = (0.5-loc[1])*0.48*((0.46 - 0.1*n)/0.46)+.06
        print([-x, -y])
        g.move([-x, -y])
        g.rob.translate_tool([0, 0, .11], 0.3, 0.3)
        g.robotiqgrip.close_gripper()
        g.rob.movej(home, 0.3, 0.3)
        g.rob.translate_tool(bin1, 0.3, 0.3)
        g.robotiqgrip.open_gripper()
        g.rob.movej(home, 0.3, 0.3)
        location.pop("apple")
        apple = False
        break

while carrot:
    #rob.movej(home, 0.2, 0.2)
    g.capture(2)
    print("Captured picture "+str(n+1))
    location = g.detect()
    print("Detection on picture "+str(n+1)+" Complete")
    if "carrot" in location and n < 2:
        loc = location["carrot"]
        x = (0.5-loc[0])*(0.64*((0.46 - 0.1*n)/0.46))
        y = (0.5-loc[1])*0.48*((0.46 - 0.1*n)/0.46)+.06*((0.46 - 0.1*n)/0.46)
        print([-x, -y])
        g.move([-x, -y])
        print("moved to "+str([-x, -y]))
        n+=1

    if n == 2 and ("carrot" in location):
        g.capture(2)
        print("Captured picture "+str(n+1))
        location = g.detect()
        print("Detection on picture "+str(n+1)+" Complete")
        loc = location["carrot"]
        x = (0.5-loc[0])*(0.64*((0.46 - 0.1*n)/0.46))+.03
        y = (0.5-loc[1])*0.48*((0.46 - 0.1*n)/0.46)+.06
        print([-x, -y])
        g.move([-x, -y])
        g.rob.translate_tool([0, 0, .11], 0.3, 0.3)
        g.robotiqgrip.close_gripper()
        g.rob.movej(home, 0.3, 0.3)
        g.rob.translate_tool(bin1, 0.3, 0.3)
        g.robotiqgrip.open_gripper()
        g.rob.movej(home, 0.3, 0.3)
        carrot = False
        break

while bottle:
    #rob.movej(home, 0.2, 0.2)
    g.capture(2)
    location = g.detect()
    if "bottle" in location and n < 2:
        loc = location["bottle"]
        x = (0.5-loc[0])*(0.64*((0.46 - 0.1*n)/0.46))
        y = (0.5-loc[1])*0.48*((0.46 - 0.1*n)/0.46)+.06*((0.46 - 0.1*n)/0.46)
        print([-x, -y])
        g.move([-x, -y])
        print("moved to "+str([-x, -y]))
        n+=1
    if n == 2 and ("bottle" in location):
        g.capture(2)
        print("Captured picture "+str(n+1))
        location = g.detect()
        print("Detection on picture "+str(n+1)+" Complete")

        loc = location["bottle"]
        x = (0.5-loc[0])*(0.64*((0.46 - 0.1*n)/0.46))+.03
        y = (0.5-loc[1])*0.48*((0.46 - 0.1*n)/0.46)+.06
        print([-x, -y])
        g.move([-x, -y])
        g.rob.translate_tool([0, 0, .11], 0.3, 0.3)
        g.robotiqgrip.close_gripper()
        g.rob.movej(home, 0.3, 0.3)
        g.rob.translate_tool(bin3, 0.3, 0.3)
        g.robotiqgrip.open_gripper()
        g.rob.movej(home, 0.3, 0.3)
        location.pop("bottle")
        bottle = False
        break

g.rob.close()