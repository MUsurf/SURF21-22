#!/usr/bin/env python3
import rospy
import yaml
from std_msgs.msg import Int32MultiArray

def publisher():
    pub = rospy.Publisher('/command', Int32MultiArray, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10)
    
    array1=[0,0,0,0,0,0,0,0,320,320,320,320,0,0,0,0]
    my_array1_for_publishing = Int32MultiArray(data=array1)

    pub.publish(my_array1_for_publishing)
    
    rospy.sleep(1)
    
    array2=[0,0,0,0,0,0,0,0,1500,1500,1500,1500,0,0,0,0]
    my_array2_for_publishing = Int32MultiArray(data=array2)
    
    pub.publish(my_array2_for_publishing)
    
    rospy.sleep(1)
    
if __name__ == '__main__':
	publisher()
