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

string = ""

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    global comm
    comm = data
    string = data
    #esc1 = comm.data[15]
    #esc1 = int(esc1)
    #print(esc1)
    
def subscriber():
    sub = rospy.Subscriber('/command',String,callback)
    rospy.init_node('controller_test', anonymous=True)
    rate = rospy.Rate(10)

    if not rospy.is_shutdown():
        rospy.sleep(1)
    
        publisher(string)
    
def publisher(string):
    pub = rospy.Publisher('test', String , queue_size=10)
    rospy.init_node('controller_test', anonymous=True)
    rate = rospy.Rate(1)
    data = string
    pub.publish(data)
    rate.sleep()
    
    subscriber()
    
    
    
if __name__ == '__main__':
    subscriber()
