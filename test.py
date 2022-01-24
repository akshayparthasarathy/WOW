import urx 
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
import time

rob = urx.Robot("192.168.1.5", True)

robotiqgrip = Robotiq_Two_Finger_Gripper(rob)

home = [0, -1.57, -1.57, -1.57, 1.57, 0]
rob.movej(home, 0.5, 0.5)

#rob.translate_tool([0, 0.4, 0], 0.1, 0.1)

# while rob.get_force() < 10:
#     rob.translate_tool([0, 0, 0.01], 0.5, 0.1)
#     time.sleep(0.05)

# robotiqgrip.close_gripper()

# time.sleep(2)

# robotiqgrip.open_gripper()

rob.close()