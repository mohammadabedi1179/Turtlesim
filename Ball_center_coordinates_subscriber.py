#!/usr/bin/python3.8

import numpy as np
import rospy
from turtlesim.msg import Pose
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist
import numpy as np


def callback_fun(msg):
    global position

    position = msg.data


def callback_fun_2(msg):
    global scaled_positions , scaled_turtle_position

    scaled_turtle_position = (msg.x/(2*5.544445),msg.y/(2*5.544445),msg.theta)
    scaled_positions = (position[0]/640,1-position[1]/480)

    velocity_publisher(scaled_turtle_position,scaled_positions)


def velocity_publisher(current,goal):

    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rot=Twist()
    theta = np.arctan2(goal[1] - current[1],goal[0] - current[0])

    x_vel = np.sqrt((goal[0] - current[0])**2+(goal[1]-current[1])**2)


    if goal == (0,1):
        rot.linear.x = 0
        rot.linear.y = 0
        rot.linear.z = 0
    
        rot.angular.x = 0
        rot.angular.y = 0
        rot.angular.z = 0
    else :

        rot.linear.x =  7 * x_vel
        rot.linear.y =  0
        rot.linear.z =  0

        rot.angular.x = 0
        rot.angular.y = 0
        rot.angular.z = 10 * (theta - current[2])
        
    rospy.loginfo(f"node is sending velocity ----{rot.linear.x}")
    
    pub.publish(rot)



def subscriber():
    rospy.init_node('subscriber')

    sub_center = rospy.Subscriber('/ball_center',Float64MultiArray,callback=callback_fun)
    sub_pose = rospy.Subscriber('/turtle1/pose',Pose,callback=callback_fun_2)
    rospy.spin()


    return()

if __name__=="__main__":

     subscriber()


