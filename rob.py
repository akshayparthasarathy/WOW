import urx
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

rob = urx.Robot("192.168.1.6")

robotiqgrip = Robotiq_Two_Finger_Gripper(rob)

home = [0, -1.57, -1.57, -1.57, 1.57, 0]

bin1 = [-0.20, 0.1, 0.21]
bin2 = [-0.20, -0.1, 0.21]
bin3 = [0.20, 0, 0.21]

def bottle(coordinates, _bin=bin1):

    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(coordinates, 0.1, 0.1)

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

    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(coordinates, 0.1, 0.1)

    robotiqgrip.close_gripper()
    print("Fruit Grabbed")

    rob.movej(home, 0.2, 0.2)
    rob.translate_tool(_bin, 0.1, 0.1)

    robotiqgrip.open_gripper()
    print("fruit Released")

    rob.movej(home, 0.2, 0.2)
    print("Fruit moving operation status: Complete")

test = [0, 0, 0.21]

bottle(test)

vegetable(test)

fruit(test)

rob.close()