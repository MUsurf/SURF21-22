#!/usr/bin/env python3
import rospy
import yaml
import numpy
# Import numpy for ROS messages to ease the extraction of data from messages
# that are arrays.
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import String

from std_msgs.msg import Int32MultiArray

def callback(data):
    print('The string I got is ' + data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    sub = rospy.Subscriber('test', String , callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()
