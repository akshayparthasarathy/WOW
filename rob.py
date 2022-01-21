import urx 
import time
import cv2 as cv
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

import json
f = open('location.json',)
location = json.load(f)
f.close()

rob = urx.Robot("192.168.1.5", True)

robotiqgrip = Robotiq_Two_Finger_Gripper(rob)

height = 480
width = 640
n = 1

home = [0, -1.57, -1.57, -1.57, 1.57, 0]

bin1 = [-0.20, 0.1, 0.21]
bin2 = [-0.20, -0.1, 0.21]
bin3 = [0.20, 0, 0.21]

def bottle(coordinates, _bin=bin1):

    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(coordinates, 0.1, 0.1)

    while rob.get_force() < 10:
        rob.translate_tool([0, 0, 0.01], 0.3, 0.3)
        time.sleep(0.05)
    robotiqgrip.close_gripper()
    print("Bottle Grabbed")

    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(_bin, 0.1, 0.1)

    robotiqgrip.open_gripper()
    print("Bottle Released")

    rob.movej(home, 0.2, 0.2)
    print("Bottle moving operation: Complete")

def vegetable(coordinates, _bin=bin2):
    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(coordinates, 0.1, 0.1)

    robotiqgrip.close_gripper()
    print("Vegetable Grabbed")

    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(_bin, 0.1, 0.1)

    robotiqgrip.open_gripper()
    print("Vegetable Released")

    rob.movej(home, 0.2, 0.2)
    print("Vegetable moving operation status: Complete")

def fruit(coordinates, _bin=bin3):
    robotiqgrip.open_gripper()
    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(coordinates, 0.1, 0.1)

    while rob.get_force() < 10:
        rob.translate_tool([0, 0, 0.01], 0.3, 0.3)
        time.sleep(0.05)

    robotiqgrip.close_gripper()
    print("Fruit Grabbed")

    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(_bin, 0.1, 0.1)

    robotiqgrip.open_gripper()
    print("Fruit Released")

    rob.movej(home, 0.2, 0.2)
    print("Fruit moving operation status: Complete")

for i in range(0, len(location)):
    if "bottle" in location:
        loc = location["bottle"]
        xmax = loc[1][0]
        xmin = loc[0][0]
        ymax = loc[0][1]
        ymin = loc[1][1]
        bottle([(xmax+xmin)/2, (ymin+ymax)/2, 0])
        location.pop("bottle")

    if "carrot" in location:
        loc = location["carrot"]
        xmax = loc[1][0]
        xmin = loc[0][0]
        ymax = loc[0][1]
        ymin = loc[1][1]
        vegetable([(xmax+xmin)/2, (ymin+ymax)/2, 0])
        location.pop("carrot")

    if "apple" in location:
        loc = location["apple"]
        xmax = -loc[1][0]
        xmin = -loc[0][0]
        ymax = 0.5 * 0.5 - loc[0][1]
        ymin = 0.5 * 0.5 - loc[1][1]
        fruit([(xmax+xmin)/2, (ymin+ymax)/2, 0])
        location.pop("apple")
# bottle(test)

# vegetable(test)

# fruit(test)

# for i in range(0, n):
#     input(0, n)

rob.close()

#try using force stop sensor