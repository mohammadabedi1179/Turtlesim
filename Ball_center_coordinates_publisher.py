#!/usr/bin/python3.8


import numpy as np
import cv2
from Open_cv import opencv
import rospy
from std_msgs.msg import Float64MultiArray

cap = cv2.VideoCapture(-1)

def open_cv():

  

  lower = np.array([97 , 71 , 150])
  upper = np.array([107 ,255, 255])

  opc = opencv()
  ret,frame=cap.read()

  binary = opc.to_binary(frame,lower,upper)

  dial = opc.enhance_binary(binary,3,15)
  frame ,center , r = opc.ball_detection(dial,frame)


  return(frame,center)


def Ball_center():
     rospy.init_node("ball_center")
     pub = rospy.Publisher("/ball_center",Float64MultiArray)
     
     
     rate = rospy.Rate(100)
     rospy.loginfo("Node is starting:   ")



     while not rospy.is_shutdown():

         frame , center = open_cv()
         data_to_send = Float64MultiArray()
         data_to_send.data = center

         if frame is None:
             break
         cv2.imshow("Frame",frame)

         key=cv2.waitKey(30)
         if key==27:
             break

        
         pub.publish(data_to_send)
         #rospy.spin()

     cap.release()
     cv2.destroyAllWindows()
    
if __name__ == "__main__":

     Ball_center()