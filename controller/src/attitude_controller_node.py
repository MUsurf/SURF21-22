#!/usr/bin/env python3

import rospy
import time
import message_filters
from sensor_msgs.msg import Imu
from ms5837.msg import ms5837_data
from std_msgs.msg import Int32MultiArray

rospy.init_node("attitude_controller_node")
rate = rospy.Rate(100)

def data_type(num):
    data = [0,0,0,0]

    for i in range(0,4):
        data[i] = num

    return data

class Controller():
    def __init__(self):
        self.imu_sub = Imu() # Paraentheses behind intialization of a message object are required.
        self.depth_sub = ms5837_data()
        self.msg = Int32MultiArray()
        self.msg.layout.dim = []
        self.msg.layout.data_offset = 16

        self.commanded = rospy.Publisher('/command', Int32MultiArray, queue_size=10)
        self.msg.data = data_type(0)

    def callbackIMU(self,data):
        self.imu_sub = data

    def callbackDepth(self,data):
        self.depth_sub = data

    def main(self):
        # print("Reached callback.")
        print(self.imu_sub.orientation.x)
        print(self.imu_sub.orientation.y)
        print(self.imu_sub.orientation.z)
        print(self.imu_sub.orientation.w)

        print(self.depth_sub.depth)

        if self.imu_sub.orientation.x > 0:
            self.msg.data = [0,1500,1550,0,0,0,0,0]
            self.commanded.publish(self.msg)
        elif self.imu_sub.orientation.x <= 0:
            self.msg.data = [0,1550,1500,0,0,0,0,0]
            self.commanded.publish(self.msg)

        
if __name__ == '__main__':
    try:
        loop = Controller()
        while not rospy.is_shutdown(): 
            rospy.Subscriber("/imu/data", Imu,loop.callbackIMU)
            rospy.Subscriber("/rov/ms5837", ms5837_data,loop.callbackDepth)

            loop.main()
            
            # print("Reached just after callback.")

            rate.sleep()

    except KeyboardInterrupt:
        print("Keyboard Interrupt")