import tensorflow_hub as hub
import cv2
import numpy
import tensorflow as tf
import pandas as pd
import urx
import time
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

class groceries:
    def __init__(self) -> None:
        self.height = 480
        self.width = 640

        self.home = [0, -1.57, -1.57, -1.57, 1.57, 0]

        self.bin1 = [-0.20, 0.1, 0.15]
        self.bin2 = [-0.20, -0.1, 0.42]
        self.bin3 = [0.20, 0, 0.42]

        self.rob = urx.Robot("192.168.1.5", True)
        self.robotiqgrip = Robotiq_Two_Finger_Gripper(self.rob)
        self.detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")
        self.labels = pd.read_csv('labels.csv',sep=';',index_col='ID')
        self.labels = self.labels['OBJECT (2017 REL.)']
    def capture(self, cam_no):
        #capture image
        #cam = cv2.VideoCapture(4)   
        cam = cv2.VideoCapture(cam_no)

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("Capture", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "frame.png"
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))

        cam.release()
        cv2.destroyAllWindows()

    def detect(self):
        frame = cv2.imread("frame.png")
        inp = cv2.resize(frame, (self.width , self.height))
        #Convert img to RGB
        rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)
        #Is optional but i recommend (float convertion and convert img to tensor image)
        rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)
        #Add dims to rgb_tensor
        rgb_tensor = tf.expand_dims(rgb_tensor , 0)
        boxes, scores, classes, num_detections = self.detector(rgb_tensor)
        pred_labels = classes.numpy().astype('int')[0]
        pred_labels = [self.labels[i] for i in pred_labels]
        pred_boxes = boxes.numpy()[0].astype('int')
        pred_scores = scores.numpy()[0]

        location = {}

        #Detect Items
        for score, (ymin,xmin,ymax,xmax), label in zip(pred_scores, pred_boxes, pred_labels):
            if score < 0.3:
                continue
                
            score_txt = f'{100 * round(score,0)}'
            img_boxes = cv2.rectangle(frame,(xmin, ymax),(xmax, ymin),(0,0,255),2)      
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img_boxes,label,(xmin, ymax-10), font, 0.5, (255,0,0), 1, cv2.LINE_AA)
            cv2.putText(img_boxes,score_txt,(xmax, ymax-10), font, 0.5, (255,0,0), 1, cv2.LINE_AA)
            if label == "carrot" or label == "bottle" or label == "apple":
                location[label] = [(xmin/self.width+xmax/self.width)/2, (ymin/self.height+ymax/self.height)/2]
        cv2.imshow("Detections", img_boxes)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return location

    def move(self, coord):
        self.rob.translate_tool(coord, 0.2, 0.2)
        self.rob.translate_tool([0, 0, 0.1], 0.2, 0.2)

    def grab(self, coord, bin):
        print("grabbing")
        self.move(coord)
        self.rob.translate_tool([0, 0, .11], 0.3, 0.3)
        self.robotiqgrip.close_gripper()
        self.rob.movej(self.home, 0.3, 0.3)
        self.rob.translate_tool(bin, 0.3, 0.3)
        self.robotiqgrip.open_gripper()
        self.rob.movej(self.home, 0.3, 0.3)