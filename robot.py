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

bin1 = [-0.20, 0.1, 0.15]
bin2 = [-0.20, -0.1, 0.42]
bin3 = [0.20, 0, 0.42]

apple = True
carrot = False
bottle = False
n=0

while apple:
    #rob.movej(home, 0.2, 0.2)
    g.capture(2)
    location = g.detect()
    if "apple" in location and n < 2:
        loc = location["apple"]
        x = (0.5-loc[0])*0.64
        y = (0.5-loc[1])*0.48+.06
        print([-x, -y])
        #g.move([-x, -y])
        print("moved to "+str([-x, -y]))
        n+=1
    if n == 1 and ("apple" in location):
        loc = location["apple"]
        x = (0.5-loc[0])*(0.64*(0.26/0.46))
        y = (0.5-loc[1])*(0.48*(0.26/0.46))+.06
        print([-x, -y])
        g.move([-x, -y])
        g.grab("apple")
        location.pop("apple")
        apple = False

while carrot:
    #rob.movej(home, 0.2, 0.2)
    g.capture(0)
    location = g.detect()
    if "carrot" in location and n < 2:
        loc = location["carrot"]
        x = (0.5-loc[0])*0.64
        y = (0.5-loc[1])*0.48+.06
        print([-x, -y])
        #g.move([-x, -y])
        print("moved to "+str([-x, -y]))
        n+=1

    if n == 2 and ("carrot" in location):
        loc = location["carrot"]
        x = (0.5-loc[0])*0.64
        y = (0.5-loc[1])*0.48+.06
        print([-x, -y])
        #g.move([-x, -y])
        #g.grab("carrot")
        location.pop("carrot")
        carrot = False

while bottle:
    #rob.movej(home, 0.2, 0.2)
    g.capture(0)
    location = g.detect()
    if "apple" in location and n < 2:
        loc = location["apple"]
        x = (0.5-loc[0])*0.64
        y = (0.5-loc[1])*0.48+.06
        print([-x, -y])
        #g.move([-x, -y])
        print("moved to "+str([-x, -y]))
        n+=1

    if n == 2 and ("bottle" in location):
        loc = location["bottle"]
        x = (0.5-loc[0])*0.64
        y = (0.5-loc[1])*0.48+.06
        print([-x, -y])
        #g.move([-x, -y])
        #g.grab("bottle")
        location.pop("bottle")
        bottle = False