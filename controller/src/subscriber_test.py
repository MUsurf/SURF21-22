#!/usr/bin/env python3

# BEGIN IMPORT
import rospy
import time
# END IMPORT

# BEGIN STD_MSGS
from std_msgs.msg import Int32MultiArray
# END STD_MSGS

def data_type(num):
    data = [0,0,0,0]

    for i in range(0,4):
        data[i] = num

    return data

rospy.init_node("subscriber_test")

# BEGIN PUB
# pub = rospy.Publisher('command', Int32MultiArray, queue_size=10)
# END PUB

# BEGIN LOOP
rate = rospy.Rate(2) # If set to 1 Hz it will be a counter of seconds

count = 0

class MainLoop():
    def __init__(self):
        self.msg = Int32MultiArray()
        self.msg.layout.dim = []
        self.msg.layout.data_offset = 16

        print("Just before data")

        self.msg.data = data_type(1700)

        self.commanded = rospy.Publisher('/command', Int32MultiArray, queue_size=10)
        
        while not rospy.is_shutdown():
            for i in range(1300,1700):
                self.msg.data = data_type(i)
                self.commanded.publish(self.msg)
                time.sleep(0.01)
            for i in range(1300,1700):
                x= (-1*i) + 3000
                self.msg.data = data_type(x)
                self.commanded.publish(self.msg)
                time.sleep(0.01)

if __name__ == '__main__':
    try:
        print("At main loop.")
        MainLoop()
        print("Beyond Main Loop")
        rospy.spin()
    except KeyboardInterrupt:
        MainLoop.msg.data = data_type(0)
        MainLoop.commanded.publish(MainLoop.msg)
# END LOOP
# END ALL
